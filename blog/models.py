from django.db import models

# Create your models here.
from bitarif_user.models import BitarifUser


class Blog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    image_link=models.URLField()
    created_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(BitarifUser, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.title
