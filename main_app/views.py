from rest_framework.views import APIView
from rest_framework.response import Response

class Home(APIView):
    def get(self, request):
        content = {'messege': 'Welcome to the jewel-collector api home route!'}
        return Response(content)