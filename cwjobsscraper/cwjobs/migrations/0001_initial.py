# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PythonJobLondon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, null=True, blank=True)),
                ('url', models.CharField(max_length=500, null=True, blank=True)),
                ('date_found', models.DateTimeField(null=True, blank=True)),
                ('date_posted', models.CharField(max_length=25, null=True, blank=True)),
                ('salary', models.CharField(max_length=250, null=True, blank=True)),
                ('employment_type', models.CharField(max_length=20, null=True, blank=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='pythonjoblondon',
            unique_together=set([('title', 'url')]),
        ),
    ]
