from django.conf import settings
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.utils.text import slugify
from django.dispatch import receiver
import secrets



class UserManager(BaseUserManager):
    def create_user(
        self,
        first_name,
        last_name,
        cellphone_no,
        password=None,
        is_active=True,
        is_staff=False,
        is_admin=False,
        is_shopowner=False,
        is_customer=False,
    ):
        if not cellphone_no:
            raise ValueError("User must have a cellphone number")

        if not password:
            raise ValueError("User must have a password")

        if not first_name:
            raise ValueError("Name is required")

        if not last_name:
            raise ValueError("Surname is required")

        user_obj = self.model(
            first_name=first_name,
            last_name=last_name,
            cellphone_no=cellphone_no,
            password=password,
        )
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_admin
        user_obj.active = is_active
        user_obj.is_shopowner = is_shopowner
        user_obj.is_customer = is_customer
        user_obj.save(using=self.db)
        return user_obj

    def create_staffuser(self, first_name, last_name, cellphone_no, password=None):
        user = self.create_user(
            first_name, last_name, cellphone_no, password=password, is_staff=True
        )
        return user

    def create_superuser(self, first_name, last_name, cellphone_no, password=None):
        user = self.create_user(
            first_name,
            last_name,
            cellphone_no,
            password=password,
            is_active=True,
            is_staff=True,
            is_admin=True,
            is_shopowner=True,
            is_customer=True,
        )
        return user

    def create_shopowner_user(
        self,
        first_name,
        last_name,
        cellphone_no,
        password=None,
        is_active=True,
        is_shopowner=True,
    ):
        user = self.create_user(
            first_name, last_name, cellphone_no, password, is_active, is_shopowner,
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=50, unique=True, null=True, blank=True)
    active = models.BooleanField(default=True)
    # staff = models.BooleanField(default=False)
    # admin = models.BooleanField(default=False)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cellphone_no = PhoneNumberField(unique=True)
    preferred_name = models.CharField(max_length=25, blank=True, null=True)

    is_shopowner = models.BooleanField("is shop owner", default=False)
    is_staff = models.BooleanField("is staff", default=False)
    is_superuser = models.BooleanField("is superuser", default=False)

    USERNAME_FIELD = "cellphone_no"
    # The fields required when a user is created.
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return str(self.cellphone_no)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_labels):
        return True

    @property
    def is_active(self):
        return self.active

class UserProfile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    profile_picture = models.ImageField(upload_to="profile_pictures")
    email = models.CharField(max_length=30, blank=True, null=True, unique=True)
    slug = models.Sl

    
