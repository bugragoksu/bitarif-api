from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='Category List'),
    path('difficulty/', DifficultyListView.as_view(), name='Difficulty List'),
    path('quantity/', QuantityListView.as_view(), name='Quantity List'),
    path('ingredient/', IngredientListView.as_view(), name='Ingredient List'),
    path('list/', RecipeListView.as_view(), name='Recipe List'),
    path('add/', add_recipe, name='Add Recipe'),
    path('like/', increase_like_count_recipe, name='Like Recipe'),

]
