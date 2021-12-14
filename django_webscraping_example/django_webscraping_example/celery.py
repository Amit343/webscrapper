from __future__ import absolute_import   #it distributed codes from modules.import
from celery import Celery
from celery.schedules import crontab
import os
os.environ.setdefault('DJANGO.SETINGS.MODULE','django_web_Scraping_example.settings')

app= Celery('django_webscraping_example')
app.conf.timezone='UTC'
app.config_from_object("django.conf :settings",namespace='Celery')
app.autodiscover_tasks()


