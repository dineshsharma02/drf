from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .mypagination import MyPaginationPage
# Create your views here.

class StudentList(ListAPIView):
    # SEE SETTINGS.PY FILE FOR GLOBAL PAGINATION 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPaginationPage
