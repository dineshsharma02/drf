from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=40)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=40)

    def create(self,vaildated_data):
        return Student.objects.create(**vaildated_data)

