from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DifficultyListView(ListAPIView):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer


class QuantityListView(ListAPIView):
    queryset = Quantity.objects.all()
    serializer_class = QuantitySerializer


class IngredientListView(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RecipeListView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = [
        'title',
        'category__name'
    ]
