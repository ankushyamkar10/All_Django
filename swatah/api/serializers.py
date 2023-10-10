from rest_framework import serializers
from .models import Task , Item

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
  class Meta :
    model = Item
    fields = ('category', 'subcategory', 'name', 'amount')
  
