from django.shortcuts import render
from functools import partial
import json
import io
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class Student_View(View):
    def get(self,request,*args,**kwargs):
        # print(request.body)
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
            # return JsonResponse(serializer.data)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu,many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
            # return JsonResponse(serializer.data)
    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        print(python_data)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created'}
        else:
            return JsonResponse(serializer.errors,safe=False)
        # res_json = json.dumps(res)
        return JsonResponse(res)
    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        # print(python_data)
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data updated'}
        else:
            return JsonResponse(serializer.errors,safe=False)
        # res_json = json.dumps(res)
        return JsonResponse(res)
    
    def delete(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        # print(python_data)
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {"msg":"data deleted"}
        return JsonResponse(res)