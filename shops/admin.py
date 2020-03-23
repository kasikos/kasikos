from django.contrib import admin
from .models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'user',)


admin.site.register(Shop, ShopAdmin)