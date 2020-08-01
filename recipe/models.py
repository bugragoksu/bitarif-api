from django.db import models

# Create your models here.
from bitarif_user.models import BitarifUser


class Category(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Difficulty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Quantity(models.Model):
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)

    def __str__(self):
        return str(self.amount) + " - " + str(self.name)


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.quantity) + " - " + str(self.name)


class Recipe(models.Model):
    user = models.OneToOneField(BitarifUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    desc = models.TextField()
    category = models.ManyToManyField(Category)
    difficulty = models.OneToOneField(Difficulty, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    image_url = models.CharField(max_length=500)
    time = models.CharField(max_length=30)
    serving = models.CharField(max_length=30)
    likes = models.IntegerField(default=0)
    created_date = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title
