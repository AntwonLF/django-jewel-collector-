from rest_framework import serializers
from .models import Jewels, Cleaning

class JewelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jewels
        fields = '__all__'
        
class CleaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaning
        fields = '__all__'