from django.db import models


class PythonJobLondon(models.Model):
    """model define the data field for the database"""
    title = models.CharField(max_length=250, null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    date_found = models.DateTimeField(null=True, blank=True)
    date_posted = models.CharField(max_length=25, null=True, blank=True)
    salary = models.CharField(max_length=250, null=True, blank=True)
    employment_type = models.CharField(max_length=500, blank=True,null=True)

    class Meta:
        """To avoid duplicate entry in the database"""
        unique_together = ('title', 'url')

    def __unicode__(self):
        return self.title