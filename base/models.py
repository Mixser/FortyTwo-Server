from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models

# Create your models here.
from rest_framework.authtoken.models import Token


class ApplicationUser(AbstractBaseUser):
    email = models.EmailField('Email', unique=True)

    USERNAME_FIELD = 'email'

    def get_token(self):
        token, created = Token.objects.get_or_create(user=self)
        return token