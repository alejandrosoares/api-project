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
