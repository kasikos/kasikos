from django.test import TestCase
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model

from shops.models import Shop
User = get_user_model()


# Create your tests here.
class ShopAPITestCase(APITestCase):
	def setUp(self):
		# Create a user
		user_obj = User(
			first_name='',
			last_name='',
			cellphone_no='',
			is_staff=False,
			is_superuser=False,
			active=True,
			is_shopowner=False,
		)
		user_obj.set_password("somerandompassword")
		user_obj.save()

		# Create a shop
		shop = Shop.objects.create(
				shop_name="Zweli's Kota Palace",
				slug="zweli-kota-palace",
				user=user_obj,
				street_name='28 Madison Street',
				town='Jeppestown',
				zip_code='1123',
				cellphone_no='+27712345678',
				description='some random description',
				logo='z-logo.png'
			)

	def test_single_user(self):
		user_count = User.objects.count()
		self.assertEqual(user_count, 1)

	def test_single_shop(self):
		shop_count = Shop.objects.count()
		self.assertEqual(shop_count, 1)