from django.shortcuts import render

from .models import PythonJobLondon


def index(request):
    # the home page for cwjobs scraper site
    python_jobs_london = PythonJobLondon.objects.order_by('-date_posted')
    context = {'python_jobs_london': python_jobs_london}
    return render(request, "cwjobs/index.html", context)