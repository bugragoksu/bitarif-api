from bitarif_user.serializers import BitarifUserSerializer
from .models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = '__all__'


class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    quantity=QuantitySerializer()
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    user=BitarifUserSerializer()
    category=CategorySerializer(many=True)
    difficulty=DifficultySerializer()
    ingredients=IngredientSerializer(many=True)

    class Meta:
        model=Recipe
        fields='__all__'