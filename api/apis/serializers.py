# Django Rest Framework
from rest_framework import serializers

# Own
from .models import Category, Api


class PopulateSerializer(serializers.Serializer):
    """Populate Serializer"""

    API = serializers.CharField(source='api', max_length=50)
    Description = serializers.CharField(source='description', max_length=120)
    Auth = serializers.CharField(
        source='auth', max_length=120, allow_blank=True)
    HTTPS = serializers.BooleanField(source='https')
    Cors = serializers.CharField(source='cors', max_length=7)
    Link = serializers.URLField(source='link')
    Category = serializers.CharField(source='category')

    def create(self, validate_data):

        category, _ = Category.objects.get_or_create(
            category=validate_data['category'])

        validate_data['category'] = category

        return Api.objects.create(**validate_data)


class ApiSerializer(serializers.Serializer):
    """Api Serializer"""

    id = serializers.IntegerField()
    api = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=120)
    auth = serializers.CharField(max_length=120)
    https = serializers.BooleanField()
    cors = serializers.CharField(max_length=7)
    link = serializers.URLField()
    category = serializers.CharField(max_length=20)



