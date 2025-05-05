from django.shortcuts import render
from django.contrib.auth import login

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import EmailAuthSerializer, ExtendedUserBaseSerializer

class EmailLoginView(APIView):
    serializer_class = EmailAuthSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({'user': ExtendedUserBaseSerializer(user).data}, status=status.HTTP_200_OK)
    
class CSRFSetter(APIView):
    def get(self, request):
        return Response({'detail': 'Setted'})