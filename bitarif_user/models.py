from django.db import models


# Create your models here.


class BitarifUser(models.Model):
    firebase_id = models.CharField(max_length=400, unique=True)
    email = models.EmailField(('Email Adress'), unique=True)
    name = models.CharField(max_length=100, blank=True, null=True, default='bitarif User')
    profile_pic = models.CharField(max_length=500, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    follower = models.ManyToManyField('self', related_name='followers', symmetrical=False,blank=True)

    def __str__(self):
        return self.email
