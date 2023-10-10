from rest_framework import serializers
from .models import Blog,Author

class BlogSerializers(serializers.ModelSerializer):
  class Meta:
    model = Blog
    fields = "__all__"

  def validate(self,data):
    special_characters = '!@#$%^&*()_+[]?/|.`~'
    if any(c in special_characters for c in data['title']):
      raise serializers.ValidationError('Name should contain any sepcial characters!')
    return data
  
  # def validate_fieldname(): also work for particular field

class AuthorSerializers(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = "__all__"


      

  # def validate(self,data):
  #   special_characters = '!@#$%^&*()_+[]?/|.`~'
  #   if any(c in special_characters for c in data['title']):
  #     raise serializers.ValidationError('Name should contain any sepcial characters!')
  #   if data['age'] < 14:
  #     raise serializers.ValidationError('Age should be greater than 14!')
  #   return data
