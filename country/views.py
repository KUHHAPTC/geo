from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from country.serializers import CountryDetailSerializer, CountrySerializer

from country.models import Country


class CountryView(APIView):
    def get(self, request, continent_id):
        countries = Country.objects.filter(continent__id=continent_id)
        serializer = CountrySerializer(countries, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class CountryDetailView(APIView):
    def get(self, request, **kwargs):
        country = get_object_or_404(klass=Country, continent__id=kwargs['continent_id'], pk=kwargs['country_id'])
        serializer = CountryDetailSerializer(country)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
