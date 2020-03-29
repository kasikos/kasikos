from django.db import models

from shops.models import Shop


# Create your models here.
class  Ingredient(models.Model):
	name = models.CharField(max_length=60)
	slug = models.SlugField(max_length=65, unique=True)

	def __str__(self):
		return self.name


class Menu(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(unique=True)
	shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
	ingredients = models.ManyToManyField(Ingredient, related_name='menu', blank=True)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	description = models.TextField(max_length=150)
	image = models.ImageField(upload_to='images/shop/menu/')
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title