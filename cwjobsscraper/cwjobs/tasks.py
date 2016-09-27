from celery.schedules import crontab
from celery.decorators import periodic_task
from bs4 import BeautifulSoup
from django.db import transaction
from django.db import IntegrityError
import requests
from django.utils import timezone
from .models import PythonJobLondon


@periodic_task(run_every=(crontab(minute='*/5')),
               name="search_python", ignore_results=True)
def search_python():
    """search for python jobs posted in London within the last 24 hours"""
    urlformat = 'http://www.cwjobs.co.uk/jobs/python/in-london?postedwithin=1&page={page}'
    for num in range(11):
        next_page = str(num)
        url = urlformat.format(page=next_page)
        b = requests.get(url)
        soup = BeautifulSoup(b.content, "html.parser")
        get_job_title = soup.find_all("div", {"class": "job-title"})
        get_date_posted = soup.find_all("meta", {"property": "datePosted"})
        get_job_salary = soup.find_all("li", {"class": "salary"})
        get_employment_type = soup.find_all("li", {"class": "job-type"})
        time = timezone.now()

        for job_title, date, job_salary, job_employment_type in map(None,
                                                                    get_job_title,
                                                                    get_date_posted,
                                                                    get_job_salary,
                                                                    get_employment_type):
            # iterate through the retrieved page to find job title, url and date posted.
            job_url = job_title.contents[3].attrs['content']
            list_job_title = job_title.contents[1].attrs['content']
            date_posted = date.attrs['content']
            salary = job_salary.text.encode("utf-8")
            employment_type = job_employment_type.text.encode("utf-8")
            date_found = time



            # Check if a job exists in the database before saving
            if not PythonJobLondon.objects.filter(title=list_job_title, url=job_url).exists():
                job = PythonJobLondon(
                    title=list_job_title,
                    url=job_url,
                    salary=salary,
                    date_posted=date_posted,
                    employment_type=employment_type,
                    date_found=date_found
                )
                job.save()


    return


