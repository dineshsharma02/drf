from numpy import delete
from rest_framework import serializers
from .models import Student

#Type3- validators
def start_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError("Name Should start with R")

class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=40, validators = [start_with_r])
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
    

    # Type1 validation - field level validation
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError("Seats full")
        return value


        

    #Type2 - object validation
    def validate(self, data):
        name = data.get('name')
        roll = data.get('roll')
        city = data.get('city')
        if name.lower()=="dinesh" and city.lower()!='bhimsar':
            raise serializers.ValidationError("Dinesh is from bhimsar.pls fill it correctly")

        if name[0:2]!="19" or name[2:5]!="BCE" or len(name)!=9:
            raise serializers.ValidationError("name should be of type 19BCEXXXX")
        return data

