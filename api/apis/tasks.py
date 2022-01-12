from __future__ import absolute_import

# Django Rest Framework
from rest_framework.decorators import api_view

# Own
from .models import Category, Api
from .serializers import PopulateSerializer

# Thrid parties
import requests
from celery import shared_task

URL_API = 'https://api.publicapis.org/entries'


@shared_task(bind=True)
def populate_db(self):

    res = requests.get(URL_API)

    if res.status_code == 200:
        content = res.json()

        entries = content['entries']

        for row in entries:

            serializer = PopulateSerializer(data=row)

            if serializer.is_valid():
                serializer.save()
