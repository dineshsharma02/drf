from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend # for local filtering

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','city']
    # fiterset_fields = ['city']
    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)
