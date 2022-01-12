# Django Rest Framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Own
from .serializers import ApiSerializer
from .tasks import populate_db
from .models import Category, Api


@api_view(['GET', 'POST'])
def PopulateView(request):
    """Populate View"""

    if request.method == 'POST':

        task = populate_db.apply_async(queue='populate_db')

        content = {
            'message': 'Task of populating the database has been launched'
        }
        return Response(content, status=status.HTTP_200_OK)

    elif request.method == 'GET':

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def SearchByKeywordView(request):
    """ Search APIs by KEYWORD 

    Search for APIs with their api field to start with the keyword passed
    """

    if request.method == 'POST':

        keyword = request.data.get('keyword', False)

        if keyword:

            try:

                apis = Api.objects.filter(api__istartswith=keyword)

                serializer = ApiSerializer(apis, many=True)

                return Response(serializer.data)

            except Category.DoesNotExist:
                pass

        return Response([])

    elif request.method == 'GET':

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def SearchByCategoryView(request):
    """ Search By Category 

    Search for APIs with the category passed
    """

    if request.method == 'POST':
        category = request.data.get('category', False)

        if category:
            try:
                category = Category.objects.get(category=category)

                apis = Api.objects.filter(category=category)

                serializer = ApiSerializer(apis, many=True)

                return Response(serializer.data)

            except Category.DoesNotExist:
                pass

        return Response([])

    elif request.method == 'GET':

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def OrdenedListView(request):
    """ Ordened List View 
    List APIs ordened by ID field
    """

    if request.method == 'POST':

        apis = Api.objects.all().order_by('id')

        serializer = ApiSerializer(apis, many=True)

        return Response(serializer.data)

    elif request.method == 'GET':

        return Response(status=status.HTTP_404_NOT_FOUND)
