from django.urls import path
from menu.api.views import (
	MenuView, 
	MenuAPIView, 
	# IngredientsView, 
	# IngredientsAPIView
)

app_name = "menu"
urlpatterns = [
    path("", MenuAPIView.as_view(), name="menu-create"),
    path("<slug:slug>/", MenuView.as_view(), name="menu"),
    # path("ingredients/", IngredientsAPIView.as_view(), name="ingredient-create"),
    # path("ingredients/<slug:slug>/", IngredientsView.as_view(), name="ingredients"),
]
