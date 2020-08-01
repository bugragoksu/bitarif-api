from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListAPIView


# Create your views here.


class BitarifUserListView(ListAPIView):
    queryset = BitarifUser.objects.all()
    serializer_class = BitarifUserSerializer
    lookup_field = 'firebase_id'
