from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import User
from user.serializers import UserSerializer


# Create your views here.

@api_view(['GET'])
def hi(request):
    return Response({'status': 200, 'data': 'Hello, Users!'})

class UserAPI(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=UserSerializer, operation_id='Create Personnel',
        responses={201: UserSerializer}
    )
    def post(self, request):
        # data = request.data[0]
        data = request.data
        data = data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserIDAPI(APIView):
    @swagger_auto_schema(
        request_body=UserSerializer, operation_id='Edit Personnel',
        responses={201: UserSerializer}
    )
    def put(self, request, pk):
        if pk is None:
            return Response({'error': 'User ID (id) is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if pk is None:
            return Response({'error': 'User ID (id) is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({'message': 'User Successfully deleted'})