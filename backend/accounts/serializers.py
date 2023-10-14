from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


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

    def validate_email(self, email):
        if '@' not in email:
            raise serializers.ValidationError('It is not an email. Please enter again')
        return email
    
    def validate_passwords(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwords don`t match')
        return data
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password2'])
        user.save()
        return user