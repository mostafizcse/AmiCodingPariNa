from rest_framework import serializers

from .models import Data

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ('user_id', 'timestamp', 'input_values')
