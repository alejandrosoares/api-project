# Django
from django.test import TestCase, Client
from django.urls import reverse

# Own
from .add_recors_to_db import add_records


class CategoryViewTestCase(TestCase):
    """ Category View Test Case

    Test of SearchByCategoryView
    """

    def setUp(self):
        self.url = reverse('apis:category')
        
        self.c = Client()

        add_records()

    def test_get_method(self):
        """
        GET method should return 404 status code 
        """

        res = self.c.get(self.url)

        self.assertEqual(res.status_code, 404)
    
    def test_valid_post(self):
        """
        Compares the submitted categorys with the category of responsed list
        """

        category = "Social"
        body = {
            "category": category
        }

        res = self.c.post(self.url, body)
        
        first_item = res.json()[0]
        response_category = first_item['category']

        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_category, category)

    def test_invalid_post(self):
        """
        Sending request with invalid body
        """

        body = {
            "cateeg": "Social"
        }

        res = self.c.post(self.url, body)

        self.assertEqual(res.status_code, 200)
        self.assertIn('message', res.json()) # error message