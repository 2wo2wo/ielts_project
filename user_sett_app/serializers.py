from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import User
from django_email_verification import send_email


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'password': {'required': True},
            'password2': {'required': True}
        }

    def validate_passwords(self, attrs):
        if attrs.get('password')!= attrs.get('password2'):
            raise serializers.ValidationError({"passwords": "your  passwords do not match"})
        return attrs




    def create(self, validated_data):
        password2 = validated_data.pop('password2', None)
        instance = self.Meta.model(**validated_data)
        instance.set_password(validated_data.get('password'))
        instance.is_active = False
        send_email(instance)
        print('email sended')
        instance.save()
        return instance

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password', 'password2', 'old_password')


    def validate(self,attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError('{"error": "Passwords should match"}')
        return attrs

    def validation_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password":"your current password did not match"})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user
        # user can edit only his profile
        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.save()
        return instance

class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'last_name', 'first_name')
        extra_kwargs = {
            'last_name': {"required":True},
            'first_name': {"required":True}
        }

    def validate_email(self, value):
        user = self.context['request'].user
        print(user)
        if User.objects.exclude(pk=user.pk).filter(email=user.username).exists():
            raise serializers.ValidationError({"email":"Email already exists"})
        return value

    def validate_username(self, value):
        user = self.context["request"].user
        if User.objects.exclude(pk=user.pk).filter(username=user.username).exists():
            raise serializers.ValidationError({"username": "Username already exists"})
        return value

    def update(self, instance,  validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        # instance.is_active = False
        # send_email(instance)   ## If you want add send_email and activate feature
        instance.email = validated_data.get('email')

        return instance





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'username': {'required': True},
            'password': {'required': True},
            'email': {'required': True}
        }