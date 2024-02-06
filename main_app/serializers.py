from rest_framework import serializers
from .models import Jewels, Cleaning, Collector

        
class CleaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaning
        fields = '__all__'

class CollectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collector
        fields = ['id', 'name', 'email'] 
        
class JewelsSerializer(serializers.ModelSerializer):
    collectors = CollectorSerializer(many=True, read_only=True)

    class Meta:
        model = Jewels
        fields = ['id', 'name', 'material', 'price', 'description', 'color', 'collectors']