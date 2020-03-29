from django.urls import path
from menu.api.views import (
	MenuView, 
	MenuAPIView, 
	IngredientView, 
	IngredientsAPIView
)

app_name = "menu"
urlpatterns = [
    path("", MenuAPIView.as_view(), name="menu-create"),
    path("ingredients/", IngredientsAPIView.as_view(), name="ingredient-create"),
    path("<slug:slug>/", MenuView.as_view(), name="menu"),
    path("ingredients/<slug:slug>/", IngredientView.as_view(), name="ingredients"),
]
