from rest_framework import serializers
from django.contrib.auth.models import User
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
    user = serializers.ReadOnlyField(source='user.username')  # Include the user field

    class Meta:
        model = Jewels
        fields = ['id', 'name', 'material', 'price', 'description', 'color', 'collectors', 'user']  # Add 'user' to fields

class UserSerializer(serializers.ModelSerializer):
    jewels = serializers.PrimaryKeyRelatedField(many=True, queryset=Jewels.objects.all())  # To show jewels owned by the user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'jewels']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new user with encrypted password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
