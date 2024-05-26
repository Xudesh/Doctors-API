from django.shortcuts import render
from .models import API
from .serializers import APISerializer
from rest_framework import generics


class APIView(generics.ListAPIView):
    queryset = API.objects.all()
    serializer_class = APISerializer