from .models import *
from rest_framework import serializers


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitarifUser
        fields = ('firebase_id',)


class BitarifUserSerializer(serializers.ModelSerializer):
    follower = FollowerSerializer(many=True)

    class Meta:
        model = BitarifUser
        fields = '__all__'


class BitarifUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitarifUser
        fields = '__all__'


class BitarifUserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitarifUser
        fields = ('firebase_id', 'name',)
