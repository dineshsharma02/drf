from functools import partial
from telnetlib import STATUS
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data,status= status.HTTP_400_BAD_REQUEST)

    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None,format=None):
        id  = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data updated'})
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk=None,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data deleted'})

    def patch(self,request,pk=None,format=None):
        id  = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data updated'})
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)





# @api_view(['GET','POST','PUT','DELETE','PATCH'])
# def student_api(request,pk=None):
#     if request.method=="GET":
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id = id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu,many=True)
#         return Response(serializer.data,status= status.HTTP_400_BAD_REQUEST)

#     if request.method=="POST":
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'data created'},status= status.HTTP_201_CREATED)
#         return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

#     if request.method=="PUT":
#         id  = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data updated'})
#         return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

#     if request.method=="DELETE":
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data deleted'})

#     if request.method=="PATCH":
#         id  = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Data updated'})
#         return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)


