from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from continent.models import Continent
from continent.serializers import ContinentSerializer


class ContinentView(APIView):
    def get(self, request):
        continents = Continent.objects.all()
        serializer = ContinentSerializer(continents, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ContinentDetailView(APIView):
    def get(self, request, continent_id):
        continent = get_object_or_404(klass=Continent, pk=continent_id)
        serializer = ContinentSerializer(continent)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
