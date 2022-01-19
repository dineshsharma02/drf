from nbformat import read
from rest_framework import serializers
from .models import Student


# Type3- validators
def start_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError("Name Should start with R")

# #only this can handle serializers
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['name','roll','city']


class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True) # to make this field read only -->method 1
    name = serializers.CharField(validators=[start_with_r]) # to assign a validator
    class Meta:
        model = Student
        fields = ['name','roll','city']
        #read_only_fields = ['name','roll'] # to make this field read only -->method 2
       # extra_kwargs = {'name':{'read_only':True}} # to make this field read only -->method 3

    # Type1 validation - field level validation
    # def validate_roll(self,value):
    #     if value>=200:
    #         raise serializers.ValidationError("Seats full")
    #     return value


        

    #Type2 - object validation
    def validate(self, data):
        name = data.get('name')
        roll = data.get('roll')
        city = data.get('city')
        if name.lower()=="dinesh" and city.lower()!='bhimsar':
            raise serializers.ValidationError("Dinesh is from bhimsar.pls fill it correctly")
        return data

    #     if name[0:2]!="19" or name[2:5]!="BCE" or len(name)!=9:
    #         raise serializers.ValidationError("name should be of type 19BCEXXXX")
    #     return data