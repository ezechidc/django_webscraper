
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('cwjobs.urls', namespace='cwjobs')),
url(r'^contact/', include('contact.urls', namespace='contact')),
    url(r'^users/', include('users.urls', namespace='users')),
]
