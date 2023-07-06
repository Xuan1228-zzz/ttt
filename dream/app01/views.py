from django.shortcuts import render
from .models import Users,Things,Eq,Exercise


# Create your views here.
from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response
from .serializers import UsersSerializers,EqSerializers,ThingsSerializers,ExerciseSerializers

class UsersView(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers
        
class ThingsView(ModelViewSet):
    queryset = Things.objects.all()
    serializer_class = ThingsSerializers
        
class EqView(ModelViewSet):
    queryset = Eq.objects.all()
    serializer_class = EqSerializers
        
class ExerciseView(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializers
