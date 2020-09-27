from django.db import models


# Create your models here.


class BitarifUser(models.Model):
    firebase_id = models.CharField(max_length=400, unique=True)
    email = models.EmailField(('Email Adress'), unique=True)
    password = models.CharField(max_length=500)
    name = models.CharField(max_length=100, blank=True, null=True, default='bitarif User')
    profile_pic = models.CharField(max_length=500, default="https://www.tenforums.com/geek/gars/images/2/types/thumb_15951118880user.png")
    created_date = models.DateTimeField(auto_now_add=True)
    follower = models.ManyToManyField('self', related_name='followers', symmetrical=False, blank=True)
    is_authenticated = True

    def __str__(self):
        return self.email
