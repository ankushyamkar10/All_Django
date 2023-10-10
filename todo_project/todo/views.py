from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import BlogSerializers,AuthorSerializers
from .models import Blog,Author,RegisterSerializer,LoginSerializer
from rest_framework.decorators import api_view, action, APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

class BlogViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    serializer_class = BlogSerializers
    queryset = Blog.objects.all()

    def list(self,request):
        search = request.GET.get('author')
        try:
            queryset = self.queryset
            if search :
                queryset = queryset.filter(author=search)
        
            page = request.GET.get('page',1)
            page_size = 2
            paginator = Paginator(queryset,page_size)  
            try:
                current_page = paginator.page(page)
            except PageNotAnInteger:
                return Response({'message':'Invalid page Number! Page number must be an ineteger.'})
        except EmptyPage:
            return Response({'message':'Invalid page! Page number is out of range.'})
        
        if not search:
            serializer = BlogSerializers(current_page,many=True)
            return Response(serializer.data)
        
        authors = AuthorSerializers(Author.objects.all(),many=True).data
        authors_ids = [str(obj['id']) for obj in authors]

        if not search in authors_ids:
            return Response(status=status.HTTP_404_NOT_FOUND, data = 'Author does not exists!')
        
        serializer = BlogSerializers(current_page,many=True)
        return Response(serializer.data)
            
        



class AuthorViewSet(ModelViewSet):
  serializer_class = AuthorSerializers
  queryset = Author.objects.all()

class RegisterAPI(APIView):
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        
        if not serializer.is_valid():
            return Response({'status':False,'message':serializer.errors},status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response({'status':True,'message':serializer.data},status.HTTP_201_CREATED)
    
class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)

        if not serializer.is_valid():
            return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.data['username']
        password = serializer.data['password']

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'status': False, 'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        token,_ = Token.objects.get_or_create(user=user)

        return Response({'status': True, 'message': 'Login successful', 'token': str(token)}, status=status.HTTP_200_OK)


#   @action(detail=True, methods=['GET'])
#   def blogs(self, request, pk=None):
#     author = self.get_object()
#     blogs = Blog.objects.filter(author=author)
#     serializer = BlogSerializers(blogs, many=True)
#     return Response(serializer.data)

#   def list(self,request):
#       blogs = Blog.objects.all()
#       serializer = BlogSerializers(blogs,many=True)
#       return Response(serializer.data)
  
#   def create(self, request):
#       serializer = BlogSerializers(data=request.data)
#       if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data, status=status.HTTP_201_CREATED)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
#   def retrieve(self,request,pk):
#       try:
#           blog = Blog.objects.get(pk=pk)
#       except Blog.DoesNotExist:
#           return Response(status=status.HTTP_404_NOT_FOUND)
#       serializer = BlogSerializers(blog)
#       return Response(serializer.data)
  
  # def create(self,request):
  #   serializer = BlogSerializers(data=request.data)
  #   if serializer.is_valid():
  #       serializer.save()
  #       return Response(serializer.data,status=status.HTTP_201_CREATED)
  #   return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','POST'])
# def index(request):
#     if request.method == 'GET':
#         blogs = Blog.objects.all()
#         serializer = BlogSerializers(blogs,many=True)
#         return Response(serializer.data)
#     else:
#         blog = request.data
#         serializer = BlogSerializers(data=blog)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','PATCH','DELETE'])
# def singleBlog(request,pk):
    # if request.method == 'GET':
    #     try:
    #         blog = Blog.objects.get(pk=pk)
    #     except Blog.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     serializer = BlogSerializers(blog)
    #     return Response(serializer.data)
    # elif request.method == 'PATCH':
    #     try:
    #         blog = Blog.objects.get(pk=pk)
    #     except Blog.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     serializer = BlogSerializers(blog,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()    
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)
    # else:
    #     try:
    #         blog = Blog.objects.get(pk=pk)
    #     except Blog.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     blog.delete()
    #     return Response('Blog deleted!')



    


