from django.urls import path
from .views import home, recipe_detail, add_recipe

urlpatterns = [
    path('', home, name='home'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('add/', add_recipe, name='add_recipe'),
]