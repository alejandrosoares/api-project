# Django
from django.urls import path

# Own
from .views import (
    PopulateView,
    SearchByKeywordView,
    SearchByCategoryView
)

app_name = "apis"
urlpatterns = [
    path('populate-apis', PopulateView, name="populate"),
    path('keyword', SearchByKeywordView, name="keyword"),
    path('category', SearchByCategoryView, name="category"),
]