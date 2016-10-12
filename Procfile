web: gunicorn cwjobsscraper.wsgi --log-file -
worker: python manage.py celeryd -B -l info
worker: