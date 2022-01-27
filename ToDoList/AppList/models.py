from enum import Enum
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
import datetime


# Create your models here.
class UserProfileManager(BaseUserManager):
    """manager para pefiles de usuario"""
    def create_user(self , email , name , password):
        """crear nuevo user_profile"""
        if not email:
            raise ValueError('El usuario debe tener un email')

        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Modelo base de datos para usuarios en el sistema"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        #Obtener nombre completo
        return self.name

    def get_short_name(self):
        #Obtener nombre corto del usuario
        return self.name

    def __str__(self):
    #Retornan cadena representando nuestro usuario
        return self.email

IS_DONE_STATUS=(
    ('p','Pendiente'),
    ('ep','En proceso'),
    ('r','Realizada'),
)

class Task(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    task_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    is_done = models.CharField(max_length=2, choices=IS_DONE_STATUS, default="p")

    def __str__(self):
        return self.task_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


