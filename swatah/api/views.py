from django.shortcuts import render ,get_object_or_404 ,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task , Item
from .serializers import TaskSerializer , ItemSerializer
from rest_framework import serializers , status

# Create your views here.
@api_view(['GET'])
def getData(request):
  tasks = Task.objects.all()
  serializer = TaskSerializer(tasks,many=True)
  return Response(serializer.data)

@api_view(['POST'])
def postData(request):
  serializer = TaskSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['GET'])
def ApiOverView(request):
  api_urls = {
        "all_items": "/",
        "Search by Category": "/?category=category_name",
        "Search by Subcategory": "/?subcategory=category_name",
        "Add": "/create",
        "Update": "/update/pk",
        "Delete": "/item/pk/delete"
    }
  return Response(api_urls)


@api_view(['POST'])
def add_item(request):
  item = ItemSerializer(data=request.data)

  if Item.objects.filter(**request.data).exists():
    raise serializers.ValidationError('This data already exists')

  if item.is_valid():
    item.save()
    return Response(item.data)
  else:
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_items(request):
  query = request.query_params

  if query :
    items = Item.objects.filter(**query.dict())
  else :
    items = Item.objects.all()

  if items :
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)
  else:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
@api_view(['POST'])
def update_item(request,pk):
  item = Item.objects.get(pk=pk)
  updateditem = ItemSerializer(instance=item, data=request.data, partial=True)

  if updateditem.is_valid():
    updateditem.save()
    return Response(updateditem.data)
  else:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  
@api_view(['DELETE'])
def delete_item(request,pk):
  item = get_object_or_404(Item, pk=pk)
  
  item.delete()
  return Response(status=status.HTTP_202_ACCEPTED)



