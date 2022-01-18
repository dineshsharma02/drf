import json
from django.shortcuts import render
import io
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api import serializers

# Create your views here.
def student_api(request):
    if request.method=="GET":
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
@csrf_exempt
def create_student(request):
    if request.method=="POST":
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



