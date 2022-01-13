# Django
from django.test import TestCase, Client
from django.urls import reverse

# Own
from .add_recors_to_db import add_records


class KeywordViewTestCase(TestCase):
    """ Keyword View Test Case

    Test of SearchByKeywordView
    """

    def setUp(self):
        self.url = reverse('apis:keyword')
        
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
        Compares the submitted "a" keyword with the first letter
        of the api field
        """

        keyword = "a"
        body = {
            "keyword": keyword
        }

        res = self.c.post(self.url, body)
        
        first_item = res.json()[0]
        first_letter = first_item['api'][:1].lower()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(first_letter, keyword)

    def test_invalid_post(self):
        """
        Sending request with invalid body
        """

        body = {
            "invalid": "a"
        }

        res = self.c.post(self.url, body)

        self.assertEqual(res.status_code, 200)
        self.assertIn('message', res.json()) # error message