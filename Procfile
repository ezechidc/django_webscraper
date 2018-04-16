web: gunicorn cwjobsscraper.wsgi --log-file -
# worker: python manage.py celeryd -B -l debug
worker: celery -A cwjobsscraper worker -B --loglevel=debug