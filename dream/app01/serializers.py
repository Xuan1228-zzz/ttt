from .models import Users,Things,Eq,Exercise
from rest_framework import serializers

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class ThingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Things
        fields = '__all__'

class EqSerializers(serializers.ModelSerializer):
    class Meta:
        model = Eq
        fields = '__all__'
        
class ExerciseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'