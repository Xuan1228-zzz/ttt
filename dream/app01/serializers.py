from .models import Users,Things,Eq,Exercise
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
# from django.contrib.auth.password_validation import validate_password
# from django.contrib.auth.models import User


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class RegisterSeializers(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Users.objects.all())], #驗證username沒重複
    )
    password = serializers.CharField(
        write_only=True, 
        required=True,
        # validators=[validate_password],
        style={'input_type': 'password'},
    )
    email = serializers.EmailField(
        write_only=True,
        required=True
    )
    phone = serializers.CharField(
        min_length=8, 
        max_length=10, 
        write_only=True,
    )
    wallet_addr = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Users.objects.all())],
    )

    class Meta:
        model = Users
        fields =('username','password','email','phone','weight','height'
                 ,'sex','birth','wallet_addr')
        
    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})

    #     return attrs

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