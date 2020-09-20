from bitarif_user.serializers import BitarifUserNameSerializer
from .models import *
from rest_framework import serializers, exceptions


class BlogSerializer(serializers.ModelSerializer):
    author = BitarifUserNameSerializer()

    class Meta:
        model = Blog
        fields = '__all__'


class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'desc', 'image_link', 'text','firebase_id')

    def create(self, validated_data):
        print(validated_data)
        firebase_id = validated_data['firebase_id']
        try:
            user = BitarifUser.objects.get(firebase_id=firebase_id)
            blog = Blog.objects.create(author=user, **validated_data)
            return blog
        except BitarifUser.DoesNotExist:
            raise exceptions.AuthenticationFailed
