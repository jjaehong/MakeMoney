from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your views here.

@api_view(['POST'])
def update(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    
@api_view(['get'])
def user(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserSerializer(user, partial=True)
    return Response(serializer.data)