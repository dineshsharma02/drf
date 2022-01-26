from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from api import serializers


# Create your views here.
class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # LOCAL AUTHENTICATION USING BasicAuthentication
    # IN SETTINGS.PY FILE WE HAVE PLACED GLOBAL AUTHENTICATION
    authentication_classes = [TokenAuthentication]

    permission_classes = [IsAuthenticated] 
            