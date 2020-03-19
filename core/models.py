from django.conf import settings
from django.utils import timezone
from django.db import models
from django.contrib.auth.models.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
import secrets


class UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        first_name,
        last_name,
        password=None,
        is_active=True,
        is_staff=False,
        is_admin=False,
        is_shop_owner=False,
    ):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a name")
        if not last_name:
            raise ValueError("User must have a surname")
        user_obj = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_admin
        user_obj.is_shop_owner = is_shop_owner
        user_obj.is_active = is_active
        user_obj.save(using=self.db)
        return user_obj

    def create_staffuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email,
            first_name,
            last_name,
            password=password,
            is_staff=True,
            is_admin=True,
            is_shop_owner=False,
        )
        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, null=True)
    cellphone_number = PhoneNumberField(null=False, blank=True, unique=True)
    active = models.BooleanField(default=True)
    is_staff = models.BooleanField("is staff", default=False)
    is_shop_owner = models.BooleanField("is shop owner", default=False)
    is_superuser = models.BooleanField("is superuser", default=False)

    USERNAME_FIELD = "cellno"
    REQUIRED_FIELDS = ["first_name", "last_name", "cellphone_number"]

    objects = UserManager()

    def __str__(self):
        return self.cellphone_number

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return f"{self.first_name}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_labels):
        return True

    @property
    def is_active(self):
        return self.active


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="profile_pictures")