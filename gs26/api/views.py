from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from rest_framework.filters import SearchFilter

# Create your views here.
class StudentList(ListAPIView):

    # for default declaration of search filter go to settings.py
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    # search_fields = ['name','city'] # for many fields searching
    search_fields = ['city']  #only 1 field
    # search_fields = ['^city'] #starts with
    # search_fields = ['=city'] # matchs with
    # search_fields = ['city']
   
