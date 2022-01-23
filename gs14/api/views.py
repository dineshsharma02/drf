from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response

from api import serializers


# Create your views here.
class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

            