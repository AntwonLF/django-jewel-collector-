from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Jewels, Cleaning
from .serializers import JewelsSerializer, CleaningSerializer

class Home(APIView):
    def get(self, request):
        content = {'messege': 'Welcome to the jewel-collector api home route!'}
        return Response(content)
    
class JewelsList(generics.ListCreateAPIView):
  queryset = Jewels.objects.all()
  serializer_class = JewelsSerializer

class JewelsDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Jewels.objects.all()
  serializer_class = JewelsSerializer
  lookup_field = 'id'

class CleaningListCreate(generics.ListCreateAPIView):
    serializer_class = CleaningSerializer

    def get_queryset(self):
        """
        Returns a list of all the cleanings for the jewel
        as determined by the jewel_id portion of the URL.
        """
        jewel_id = self.kwargs['jewel_id']
        return Cleaning.objects.filter(jewel_id=jewel_id)

    def perform_create(self, serializer):
        """
        Associates Cleaning with the specified Jewel before saving.
        """
        jewel_id = self.kwargs['jewel_id']
        jewel = Jewels.objects.get(pk=jewel_id)
        serializer.save(jewel=jewel)

# View for retrieving, updating, and deleting a specific Cleaning record
class CleaningDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cleaning.objects.all()
    serializer_class = CleaningSerializer
    lookup_field = 'pk'

class CleaningsOnDateListView(generics.ListAPIView):
    serializer_class = CleaningSerializer

    def get_queryset(self):
        """
        Optionally filters the queryset by date, passed as a query parameter.
        """
        query_date = self.request.query_params.get('date', None)
        if query_date:
            return Cleaning.objects.filter(date=query_date)
        return Cleaning.objects.none() 