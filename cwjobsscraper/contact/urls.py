from django.conf.urls import url
from . import views

urlpatterns = [
    # contact form url
    url(r'^contact/$', views.contact, name='contact'),
]