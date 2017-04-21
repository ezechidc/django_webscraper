# django_webscraper

This is a simple project to show how to extract information(web scraping)
form a website using the following:

1) Django
2) Beautifulsoup4
3) Request
4) Celery
5) Postgres
6) Bootstrap3

A python function was written to extract and store in database the
following information for python jobs posted in London within the
last 24 hours at www.cwjobs.co.uk using request and beautifullsoup4.

1) Job Title
2) Url of the job
3) Advertised salary
4) Employment type
5) Date job was posted

A celery tasks was then hooked to the function to search for new job posted
on the website every 5 minutes. Django was then used to store, retrieve
and process the information for viewing on a web browser.

heroku link:https://cwjobsscraper.herokuapp.com
Please register and login to be able to use the app.
