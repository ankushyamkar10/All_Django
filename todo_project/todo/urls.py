from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet,AuthorViewSet,RegisterAPI,LoginAPI

router = DefaultRouter()
router.register(r'blogs',BlogViewSet,basename='blogs')
router.register(r'author',AuthorViewSet,basename='blogs')

urlpatterns = [
    path('',include(router.urls)),
    path('register/',RegisterAPI.as_view()),
    path('login/',LoginAPI.as_view())
]
