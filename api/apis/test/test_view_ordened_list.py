# Django
from django.test import TestCase, Client
from django.urls import reverse

# Own
from .add_recors_to_db import add_records

# Third parties 
from json import loads


class OrdenedListViewTestCase(TestCase):
    """ Ordened List View Test Case 

    Test of OrdenedListView
    """

    def setUp(self):
        self.url = reverse('apis:ordened-list')
        
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
        Compares id field of first and second items
        """

        res = self.c.post(self.url)
        
        json_response = res.json()

        first_item = json_response[0]
        secord_item = json_response[1]

        self.assertEqual(res.status_code, 200)
        self.assertTrue(first_item['id'] < secord_item['id'])
