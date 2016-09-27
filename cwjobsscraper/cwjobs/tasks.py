from celery.schedules import crontab
from celery.decorators import periodic_task
from bs4 import BeautifulSoup
import requests
from django.utils import timezone

from .models import PythonJobLondon


def build_job_search_url():
    """search for python jobs posted in London within the last 24 hours"""
    urlformat = 'http://www.cwjobs.co.uk/jobs/python/in-london?postedwithin=1&page={page}'
    url = []
    for num in range(11):
        next_page = str(num)
        url.append(urlformat.format(page=next_page))
    return url


@periodic_task(run_every=(crontab(minute='*/5')),
               name="get_job_details", ignore_results=True)
def get_job_details():
    time = timezone.now()
    for url in build_job_search_url():
        b = requests.get(url)
        soup = BeautifulSoup(b.content, "html.parser")
        get_job_title = soup.find_all("div", {"class": "job-title"})
        get_date_posted = soup.find_all("meta", {"property": "datePosted"})
        get_job_salary = soup.find_all("li", {"class": "salary"})
        get_employment_type = soup.find_all("li", {"class": "job-type"})

        for list_of_job_title, date, job_salary, \
            job_employment_type in map(None, get_job_title, get_date_posted,
                                       get_job_salary, get_employment_type):
            # iterate through the retrieved page to find job title, url and date posted.
            job_url = list_of_job_title.contents[3].attrs['content']
            job_title = list_of_job_title.contents[1].attrs['content']
            date_posted = date.attrs['content']
            salary = job_salary.text.encode("utf-8")
            employment_type = job_employment_type.text.encode("utf-8")
            date_found = time

            # Check if a job exists in the database before saving
            if not PythonJobLondon.objects.filter(title=job_title, url=job_url).exists():
                job = PythonJobLondon(
                    title=job_title,
                    url=job_url,
                    salary=salary,
                    date_posted=date_posted,
                    employment_type=employment_type,
                    date_found=date_found
                )
                job.save()
    return
