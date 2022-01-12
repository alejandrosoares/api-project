# Django
from django.urls import path

# Own
from .views import (
    PopulateView,
    SearchByKeywordView
)

app_name = "apis"
urlpatterns = [
    path('populate-apis', PopulateView, name="populate"),
    path('keyword', SearchByKeywordView, name="keyword"),
    
]