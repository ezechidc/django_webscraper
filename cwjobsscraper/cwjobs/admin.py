from django.contrib import admin
from .models import PythonJobLondon


class PythonJobLondonAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary', 'date_posted', 'date_found')

admin.site.register(PythonJobLondon, PythonJobLondonAdmin)

