
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, Email, password=None):
        if not Email:
            raise ValueError("Users must have an email address")

        user = self.model(
                Email=self.normalize_email(Email),

            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Email, password):
        user = self.create_user(
            Email=self.normalize_email(Email),
            password=password,

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    Email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    First_name = models.CharField(max_length=60)
    Last_name = models.CharField(max_length=60)
    Sex = models.CharField(max_length=60)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    data_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'Email'


    object = MyAccountManager()

    def __str__(self):
        return self.Email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

