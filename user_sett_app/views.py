from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import UserSerializer,RegistrationSerializer,ChangePasswordSerializer, UpdateUserSerializer
from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response
from rest_framework import views
# Create your views here.

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny,)



class ChangePasswordAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated, )

class UpdateUserProfileAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = (IsAuthenticated,)