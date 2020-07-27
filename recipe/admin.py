from django.contrib import admin

# Register your models here.
from recipe.models import *

admin.site.register([Recipe,Category,Quantity,Ingredient,Difficulty])