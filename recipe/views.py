import json
from http import HTTPStatus

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from const import *
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


@permission_classes([AllowAny])
class RecipeListView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = [
        'title',
        'category__name',
        'user__firebase_id'
    ]


@csrf_exempt
@api_view(['POST'])
def add_recipe(request):
    try:
        firebase_id = request.data['firebase_id']
        title = request.data['title']
        desc = request.data['desc']
        category_txt = request.data['category']
        difficulty_txt = request.data['difficulty']
        ingredient_list = request.data['ingredients']
        image_url = request.data['image_url']
        time = request.data['time']
        serving = request.data['serving']
    except IndexError:
        return JsonResponse({"success": False, "message": MISSING_PARAMS})

    try:
        user = BitarifUser.objects.get(firebase_id=firebase_id)
    except BitarifUser.DoesNotExist:
        return JsonResponse({"success": False, "message": USER_NOT_FOUND_TEXT})
    try:
        category = Category.objects.get(name=category_txt)
    except Category.DoesNotExist:
        return JsonResponse({"success": False, "message": CATEGORY_NOT_FOUND_TEXT})
    try:
        difficulty = Difficulty.objects.get(name=difficulty_txt)
    except Category.DoesNotExist:
        return JsonResponse({"success": False, "message": DIFFICULTY_NOT_FOUND_TEXT})
    try:

        ingredient_obj_list = []
        for ingredients in ingredient_list:
            quantity, created = Quantity.objects.get_or_create(name=ingredients["quantity"]["name"],
                                                               amount=ingredients["quantity"]["amount"])
            ingredient, created = Ingredient.objects.get_or_create(name=ingredients["name"], quantity=quantity)
            ingredient_obj_list.append(ingredient)
    except Ingredient.DoesNotExist:
        return JsonResponse({"success": False, "message": INGREDIENT_NOT_FOUND_TEXT})

    recipe = Recipe()
    recipe.user = user
    recipe.difficulty = difficulty
    recipe.desc = desc
    recipe.image_url = image_url
    recipe.serving = serving
    recipe.time = time
    recipe.title = title
    recipe.save()
    recipe.category.add(category)
    recipe.ingredients.set(ingredient_obj_list)

    serialized_obj = RecipeSerializer(recipe)
    return JsonResponse({"success": True, "data": serialized_obj.data})


@api_view(['POST'])
def increase_like_count_recipe(request):
    try:
        id = request.data.get('id')
    except IndexError:
        return JsonResponse({"success": False, "message": MISSING_PARAMS})

    try:
        recipe = Recipe.objects.get(id=id)
        recipe.likes += 1
        recipe.save()
        return JsonResponse({"success": True, "message": SUCCESSFUL_TEXT})
    except Recipe.DoesNotExist:
        return JsonResponse({"success": False, "message": RECIPE_NOT_FOUND})
    except:
        return JsonResponse({"success": False, "message": SOMETHING_WENT_WRONG})


@api_view(['POST'])
def get_liked_recipes(request):
    try:
        recipe_id_list = request.data.get("recipe_id_list")
    except IndexError:
        return JsonResponse({"success": False, "message": MISSING_PARAMS})
    try:
        recipe_list = []
        for recipe_dict in json.loads(recipe_id_list):
            recipe_list.append(Recipe.objects.get(id=int(recipe_dict['id'])))
        serialized_obj = RecipeSerializer(recipe_list, many=True)
        return JsonResponse(serialized_obj.data,safe=False)
    except Recipe.DoesNotExist:
        return JsonResponse({"success": False, "message": RECIPE_NOT_FOUND})
    except:
        return JsonResponse({"success": False, "message": SOMETHING_WENT_WRONG})
