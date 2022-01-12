from django.db import models


class Category(models.Model):
    """Category Model"""

    category = models.CharField('Category', max_length=20)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


class Api(models.Model):
    """Api Model"""

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    api = models.CharField('Api', max_length=60)
    description = models.CharField('Description', max_length=120)
    auth = models.CharField('Auth', max_length=15, blank=True, null=True)
    https = models.BooleanField('Https')
    cors = models.CharField('Cors', max_length=7)
    link = models.URLField('Link')

    class Meta:
        verbose_name = 'API'
        verbose_name_plural = 'APIs'

    def __str__(self):
        return self.api
