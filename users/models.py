# users/models.py

# Global inputs
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.db import transaction, models
from rest_framework import serializers
from django.db.models.signals import post_save
from mongoengine import Document, EmbeddedDocument, fields


class UserManager(BaseUserManager):
 
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise
 
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
 
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
 
        return self._create_user(email, password=password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
 
    """
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now=True)
    phone = models.CharField(max_length=18, default="", blank=True)
    
    is_definer = models.BooleanField(default=True)
    is_reviewer = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)

    def __str__(self):
        self.name = f"{self.last_name}, {self.first_name}"
        return self.name  

    objects = UserManager()
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
 
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
 
class UserSerializer(serializers.ModelSerializer):
 
    date_joined = serializers.ReadOnlyField()
 
    class Meta(object):
        model = User
        exclude = ()
        extra_kwargs = {'password': {'write_only': True}}


class Editor(Document):
    first_name = fields.StringField(max_length=250)
    last_name = fields.StringField(max_length=250)
    email = fields.EmailField(max_length=250)
    
    is_definer = fields.BooleanField(default=True)
    is_reviewer = fields.BooleanField(default=False)
    is_publisher = fields.BooleanField(default=False)