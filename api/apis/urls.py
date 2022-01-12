# Django
from django.urls import path

# Own
from .views import (
    PopulateView
)

app_name = "apis"
urlpatterns = [
    path('populate-apis', PopulateView, name="populate")
]