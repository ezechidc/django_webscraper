from celery.schedules import crontab
from celery.decorators import periodic_task
from datetime import datetime, date, timedelta
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


def get_job_details():
    """calls build_job_search_url() and get job details like title, url,
    date_posted, date_found and employment_type"""
    time = timezone.now()
    job_details = []
    for url in build_job_search_url():
        b = requests.get(url)
        soup = BeautifulSoup(b.content, "html.parser")
        get_job_title = soup.find_all("div", {"class": "job-title"})
        get_job_title = soup.find_all("div", {"class": "job-title"})
        get_date_posted = soup.find_all("li", {"class": "date-posted"})
        get_job_salary = soup.find_all("li", {"class": "salary"})
        get_employment_type = soup.find_all("li", {"class": "job-type"})
        for _job_title, date_post, job_salary, job_employment_type in map(lambda w, x, y, z: (w, x, y, z),
                                                                          get_job_title,
                                                                          get_date_posted,
                                                                          get_job_salary,
                                                                          get_employment_type):
            job_url = _job_title.text.strip("\n")

            job_title = _job_title.text.strip("\n")
            if date_post.text.strip("\n") == 'Today':
                date_posted = date.today()
            else:
                date_posted = date.today() - timedelta(1)
            salary = job_salary.text.strip("\n")
            employment_type = job_employment_type.text.strip("\n")
            date_found = time
            job_records = {'url': job_url, 'title': job_title, 'date_posted': date_posted,
                           'salary': salary, 'employment': employment_type, 'date': date_found}
            job_details.append(job_records)
    return job_details

@periodic_task(run_every=(crontab(minute='*/5')), name="save_jobs", ignore_results=True)
def save_jobs():
    """check if jobs exists in database before saving to avoid duplicate entry"""
    for jobs in get_job_details():
         if not PythonJobLondon.objects.filter(title=jobs['title'], url=jobs['url']).exists():
                job = PythonJobLondon(
                    title=jobs['title'],
                    url=jobs['url'],
                    salary=jobs['salary'],
                    date_posted=jobs['date_posted'],
                    employment_type=jobs['employment'],
                    date_found=jobs['date']
                )
                job.save()
    return
