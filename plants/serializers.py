from rest_framework import serializers
from .models import Plant


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'   # Alternatively,can specify the fields explicitly
        read_only_fields = ['user']
