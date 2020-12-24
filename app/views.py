from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

# Create your views here.


@api_view(['GET'])
def Index(request):
    date = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    message = 'Server is live current time is'
    return Response(data=message+date, status=status.HTTP_200_OK)
