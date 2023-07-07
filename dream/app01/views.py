from django.shortcuts import render
from .models import Users,Things,Eq,Exercise


# Create your views here.
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import * 

class UsersView(GenericAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers

    def get(self, request):#查看所有

        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        
        return Response(serializer.data)

    def post(self, request):#新增(註冊)

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class UsersDetialView(GenericAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers

    def get(self, request, pk): #取得單一user資料
    
        serializer = self.get_serializer(instance=self.get_object(), many=False)

        return Response(serializer.data)
    
    # def put(self, request, pk): #更新
    #     #獲取提交的更新數據
    #     print(request.data)
    #     #建構序列化器對象
    #     serializer = self.get_serializer(instance=self.get_object(), data=request.data)
        
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data) #對instance做序列化
    #     else:
    #         return Response(serializer.errors)

    # def delete(self, request, pk): #刪除
    #     self.get_object().delete() 
    #     return Response()

class RegisterView(GenericAPIView):
    serializer_class = RegisterSeializers

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Account has been created successfully'
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response({
                'message': 'The input content is invalid'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

class ThingsView(GenericAPIView):
    queryset = Things.objects.all()
    serializer_class = ThingsSerializers

    def get(self, request):#查看所有

        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        
        return Response(serializer.data)

    def post(self, request):#新增(註冊)

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class EqView(GenericAPIView):
    queryset = Eq.objects.all()
    serializer_class = EqSerializers

    def get(self, request):#查看所有

        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        
        return Response(serializer.data)

    def post(self, request):#新增(註冊)

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class ExerciseView(GenericAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializers

    def get(self, request):#查看所有

        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        
        return Response(serializer.data)

    def post(self, request):#新增(註冊)

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
