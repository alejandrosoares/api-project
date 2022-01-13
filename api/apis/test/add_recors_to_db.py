# Own
from apis.models import Category, Api

# Third parties
from json import loads


def add_records():
    """
    Add records to the database to perform the tests
    """
    with open('./apis/test/entries.json') as f:
            entries = loads(f.read())

    for api in entries:

        category, _ = Category.objects.get_or_create(
            category=api['category'])

        api['category'] = category

        Api.objects.create(**api)