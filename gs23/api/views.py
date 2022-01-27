from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from api import serializers

from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from api.updatedthrottle import NewThrottle


# Create your views here.
class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # LOCAL AUTHENTICATION USING BasicAuthentication
    # IN SETTINGS.PY FILE WE HAVE PLACED GLOBAL AUTHENTICATION
    authentication_classes = [BasicAuthentication]

    permission_classes = [IsAuthenticatedOrReadOnly] 
    # throttle_classes = [AnonRateThrottle,UserRateThrottle]
    throttle_classes = [AnonRateThrottle,NewThrottle]  # custom throttle by adding new throtting class in app

            