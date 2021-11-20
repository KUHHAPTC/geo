from rest_framework import serializers

from continent.models import Continent


class ContinentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Continent
        fields = ('id', 'title', 'area', )
