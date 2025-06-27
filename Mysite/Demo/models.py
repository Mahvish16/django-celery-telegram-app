from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
import uuid
# Create your models here.
class RegisterUserManager(BaseUserManager):
    def create_user(self,name, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email),name=name,)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,name,email,password=None):
        user = self.create_user(name,email,password=password)
        user.is_staff = True
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class RegisterUser(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = RegisterUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']
    def __str__(self):
        return self.name
    
class EmailVerification (models.Model):
    user = models.OneToOneField("RegisterUser", on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Telegrambot(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    username = models.CharField (max_length = 50)
    def __str__(self):
        return self.username
    
