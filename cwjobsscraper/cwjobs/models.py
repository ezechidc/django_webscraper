from django.db import models


class PythonJobLondon(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    date_found = models.DateTimeField(null=True, blank=True)
    date_posted = models.CharField(max_length=25, null=True, blank=True)
    salary = models.CharField(max_length=250, null=True, blank=True)
    employment_type = models.CharField(max_length=20, blank=True,null=True)

    class Meta:
        unique_together = ('title', 'url')

    def __unicode__(self):
        return self.title