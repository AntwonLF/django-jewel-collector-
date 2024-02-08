from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework.authtoken.models import Token
from .models import Jewels, Cleaning
from .serializers import JewelsSerializer, CleaningSerializer, UserSerializer


class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the Jewel Collector API home route!'}
        return Response(content)


class JewelsList(generics.ListCreateAPIView):
    queryset = Jewels.objects.all()
    serializer_class = JewelsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Ensure that only authenticated users can create a new Jewel
        if not self.request.user.is_authenticated:
            raise PermissionDenied({'message': 'You must be logged in to add a jewel.'})
        serializer.save(user=self.request.user) 



class JewelsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jewels.objects.all()
    serializer_class = JewelsSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        # Ensure that only the owner of the jewel can update it
        jewel = self.get_object()
        if self.request.user != jewel.user:
            raise PermissionDenied({'message': 'You do not have permission to edit this jewel.'})
        serializer.save()

        


class CleaningListCreate(generics.ListCreateAPIView):
    serializer_class = CleaningSerializer

    def get_queryset(self):
        jewel_id = self.kwargs['jewel_id']
        return Cleaning.objects.filter(jewel_id=jewel_id)

    def perform_create(self, serializer):
        jewel_id = self.kwargs['jewel_id']
        jewel = Jewels.objects.get(pk=jewel_id)
        serializer.save(jewel=jewel)


class CleaningDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cleaning.objects.all()
    serializer_class = CleaningSerializer
    lookup_field = 'pk'


class CleaningsOnDateListView(generics.ListAPIView):
    serializer_class = CleaningSerializer

    def get_queryset(self):
        query_date = self.request.query_params.get('date', None)
        if query_date:
            return Cleaning.objects.filter(date=query_date)
        return Cleaning.objects.none()


class CreateUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class VerifyUserView(APIView):
    def get(self, request):
        token = request.headers.get('Authorization', None)
        if token:
            token = token.split(' ')[1]  # Assuming the token is passed as "Token <token_value>"
            try:
                token_obj = Token.objects.get(key=token)
                user = token_obj.user
                return Response({"user": UserSerializer(user).data}, status=status.HTTP_200_OK)
            except Token.DoesNotExist:
                return Response({"error": "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Authorization Token Required"}, status=status.HTTP_401_UNAUTHORIZED)
