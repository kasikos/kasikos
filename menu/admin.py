from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Ingredient, Menu


class IngredientAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"
    list_display = (
        "name",
        "slug",
    )
    prepopulated_fields = {"slug": ("name",)}


class MenuAdmin(SummernoteModelAdmin):
	summernote_fields = "__all__"
	prepopulated_fields = {"slug": ("title",)} 
		

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Menu, MenuAdmin)