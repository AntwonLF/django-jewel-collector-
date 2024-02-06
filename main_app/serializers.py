from rest_framework import serializers
from .models import Jewels

class JewelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jewels
        fields = '__all__'
