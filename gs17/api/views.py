from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated, IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

from api import serializers
from .customauth import MyPermission


# Create your views here.
class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # LOCAL AUTHENTICATION USING BasicAuthentication
    # IN SETTINGS.PY FILE WE HAVE PLACED GLOBAL AUTHENTICATION
    authentication_classes = [SessionAuthentication]

    permission_classes = [MyPermission] 
            