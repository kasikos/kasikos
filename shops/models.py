from django.db import models
from django.core.validators import RegexValidator
from core.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Shop(models.Model):
    shop_name = models.CharField("shop name", max_length=50)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_name = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    cellphone_no = PhoneNumberField()
    email = models.EmailField(max_length=150, null=True, blank=True)
    tel_number = PhoneNumberField(null=True, blank=True)
    description = models.TextField(max_length=300)

    reg_no_regex = RegexValidator(regex=r'^([\d]){1,4}\/(\d){1,6}\/(\d){1,2}$', message="Registration number must be entered in the format: '0000/000000/00'. Up to 14 characters and digits allowed!")
    reg_no = models.CharField(validators=[reg_no_regex], max_length=15, null=True, blank=True)

    logo = models.ImageField(upload_to='images/shop/logo/')

    def __str__(self):
        return self.shop_name