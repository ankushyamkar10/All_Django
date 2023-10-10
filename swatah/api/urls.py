from django.urls import path
from  . import views

urlpatterns = [
    path("task/",views.getData, name='getData' ),
    path("task/addTask/",views.postData),
    path('',views.ApiOverView),
    path('create/',views.add_item, name='add_item'),
    path('all/',views.view_items, name='view_items'),
    path('update/<int:pk>/',views.update_item,name='update_item'),
    path('delete/<int:pk>/',views.delete_item,name='delete_item')
]
