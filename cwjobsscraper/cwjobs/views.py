from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PythonJobLondon


@login_required()
def index(request):
    # the home page for cwjobs scraper site
    python_jobs_london = PythonJobLondon.objects.order_by('-date_posted')
    paginator = Paginator(python_jobs_london, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver first page
        jobs = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page
        jobs = paginator.page(paginator.num_pages)

    return render(request, 'cwjobs/index.html', {'jobs': jobs})
