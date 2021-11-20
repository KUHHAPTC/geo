from rest_framework import serializers

from continent.serializers import ContinentSerializer

from country.models import Country


class CountryDetailSerializer(serializers.ModelSerializer):
    continent = ContinentSerializer()

    class Meta:
        model = Country
        fields = ('id', 'title', 'continent', 'area', 'population', )


class CountrySerializer(serializers.ModelSerializer):
    continent = ContinentSerializer()

    class Meta:
        model = Country
        fields = ('id', 'title', 'continent', )
