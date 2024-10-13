from django.contrib.auth.models import User
from rest_framework import serializers
from myapp.models import Employee

class UserCreateSerializer(serializers.ModelSerializer):
    password1=serializers.CharField(write_only=True)
    password2=serializers.CharField(write_only=True)
    password=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["id","username","email","password1","password2","password"]

    def create(self, validated_data):
        password1=validated_data.pop("password1")
        password2=validated_data.pop("password2")
        return User.objects.create_user(**validated_data,password=password1)
    
    def validate(self, data):
        if data["password1"]!=data["password2"]:
            raise serializers.ValidationError("password mismatch")
        
        return data
    
class EmployeeSerializer(serializers.ModelSerializer):
    user_object=serializers.CharField(read_only=True)
    class Meta:
        model=Employee
        fields=["department","role","user_object"]
        