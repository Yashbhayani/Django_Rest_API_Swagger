from rest_framework.views import APIView
from rest_framework.response import Response
from .services import *

class API(APIView):
    def get(self, request):
        return Response({'status': 200, 'data': my_func()})