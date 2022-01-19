from numpy import delete
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=40)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=40)

    def create(self,vaildated_data):
        return Student.objects.create(**vaildated_data)

    def update(self, instance, validated_data):
        # return super().update(instance, validated_data)
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
    


