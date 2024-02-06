from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Jewels
from .serializers import JewelsSerializer

class Home(APIView):
    def get(self, request):
        content = {'messege': 'Welcome to the jewel-collector api home route!'}
        return Response(content)
    
class JewelsList(generics.ListCreateAPIView):
  queryset = Jewels.objects.all()
  serializer_class = JewelsSerializer

class JewelsDetial(generics.RetrieveUpdateDestroyAPIView):
  queryset = Jewels.objects.all()
  serializer_class = JewelsSerializer
  lookup_field = 'id'