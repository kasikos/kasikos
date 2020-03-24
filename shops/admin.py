from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Shop


class ShopAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('shop_name', 'user',)
    prepopulated_fields = {"slug": ("shop_name",)}


admin.site.register(Shop, ShopAdmin)