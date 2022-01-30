from django.shortcuts import render
from .serializers import SongSerializer,SingerSerializer
from rest_framework import viewsets
from .models import Singer,Song

# Create your views here.

class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
