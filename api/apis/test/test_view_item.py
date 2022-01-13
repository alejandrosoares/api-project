# Django
from django.test import TestCase, Client
from django.urls import reverse

# Own
from .add_recors_to_db import add_records

# Third parties 
from json import loads


class ItemViewTestCase(TestCase):
    """ Item View Test Case 

    Test of ItemView
    """

    def setUp(self):
        self.url = reverse('apis:item')
        
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
        Get item with pk == 1
        """

        body = {
            "pk": "1"
        }

        res = self.c.post(self.url, body)
        
        item = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertIn('id', item)
        self.assertIn('api', item)
        self.assertIn('description', item)
        self.assertIn('auth', item)
        self.assertIn('https', item)
        self.assertIn('cors', item)
        self.assertIn('link', item)
        self.assertIn('category', item)
    
    def test_invalid_post(self):
        """
        Sending request with invalid body
        """

        body = {
            "id": "1"
        }

        res = self.c.post(self.url, body)

        self.assertEqual(res.status_code, 200)
        self.assertIn('message', res.json()) # error message
