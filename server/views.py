from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from .models import tour
from .serializer import tourSerializer
from .function import filing


class tourAPIList(generics.ListAPIView):
    serializer_class= tourSerializer
    queryset = tour.objects.all()   
   

    
class FilterAPIList(APIView):
    def get(self, request):
        data = filing('filter.json')
        return Response(data)




