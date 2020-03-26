from django.db import models
from django.conf import settings

from shops.models import Shop

# Create your models here.
class Menu(models.Model):
	title = models.Charfield(max_length=100)
	slug = models.SlugField(unique=True)
	client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
	price = models.DecimalField(..., max_digits=5, decimal_places=2)
		