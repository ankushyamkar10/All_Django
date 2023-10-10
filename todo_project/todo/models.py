from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
  name = models.TextField(max_length=200)
  age = models.IntegerField()

  def __str__ (self)->str:
    return self.name
  
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__ (self)->str:
      return self.title
    
class RegisterSerializer(serializers.Serializer):
    username =serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
      print(data)
      if data['username']:
          if  User.objects.filter(username=data['username']).exists():
              raise serializers.ValidationError('Username is already taken!')
      if data['email']:
          if  User.objects.filter(email=data['email']).exists():
              raise serializers.ValidationError('Email is already registered, please login!')
      
      return data
    
    def create(self,validate_data):
        user = User.objects.create(username=validate_data['username'],password=validate_data['password'],email=validate_data['email'])
        user.set_password(validate_data['password'])
        user.save()
        return validate_data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    

