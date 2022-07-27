from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if username is None :
            raise TypeError('Username should not be blank!')

        if email is None :
            raise TypeError('email should not be blank')

        if password is None :
            raise TypeError('password should not be blank')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):

        user = self.create_user(username, email,password)
        user.is_superuser=True
        user.is_staff = True
        user.is_active = True
        user.save()

        return user



class User(AbstractUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    date_joined = models.DateTimeField(default=timezone.now, auto_created=True)
    last_login =models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()