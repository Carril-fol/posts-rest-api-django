from django.contrib.auth.password_validation import validate_password
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Profile   

class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.CharField(
        required=True, 
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        required=True,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']
        extra_kwargs = {
            'password' : {'required': True},
            'password2' : {'required': True},
            'username' : {'required' : True},
            'first_name' : {'required' : False},
            'last_name' : {'required' : False},
            'email' : {'required' : True}
        }

    def validate_email(self, validated_data):
        if '@' not in validated_data:
            raise serializers.ValidationError('It is not an email. Please enter again')
        return validated_data
    
    def validate_password2(self, password2):
        if self.initial_data['password'] != password2:
            raise serializers.ValidationError('Passwords don`t match')
        return password2
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        profile_user = Profile.objects.create(
            user=user
        )
        user.set_password(validated_data['password2'])
        user.save()
        profile_user.save()
        return user
    

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['username_profile', 'img_profile', 'genders', 'custom_genre', 'description_profile']
        read_only = ['id', 'followers', 'user']
        extra_kwargs = {
            'username_profile' : {'required': False},
            'img_profile' : {'required': False},
            'genders' : {'required' : False},
            'custom_genre' : {'required' : False},
            'description_profile' : {'required' : False},
        }

    def validate_username(self, validated_data):
        if len(validated_data['username_profile']) < 2:
            raise serializers.ValidationError('The username must be greater than 2 characters')
        return validated_data
    
    def validate_custom_genre(self, validated_data):
        if validated_data is not None:
            gender = validated_data['custom_genre']
            if len(gender) < 2:
                raise serializers.ValidationError('The gender greater than 2 letters, for example: They/Them, She/They, etc...')
        else:
            return validated_data
        return validated_data