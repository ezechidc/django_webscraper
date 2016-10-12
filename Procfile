web: gunicorn cwjobsscraper.wsgi --log-file -
# worker: python manage.py celeryd -B -l info
worker: celery -A cwjobsscraper worker -B --loglevel=info