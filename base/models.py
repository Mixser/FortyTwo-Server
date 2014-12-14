from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

# Create your models here.
from django.utils import timezone
from rest_framework.authtoken.models import Token


class ApplicationUserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self,email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class ApplicationUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email', unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = ApplicationUserManager()

    def get_short_name(self):
        return self.email

    def get_token(self):
        token, created = Token.objects.get_or_create(user=self)
        return token

    def __unicode__(self):
        return self.email


class Score(models.Model):
    user = models.ForeignKey(ApplicationUser)
    score = models.BigIntegerField()

    def __unicode__(self):
        return "%s %s" % (self.score, self.user)
