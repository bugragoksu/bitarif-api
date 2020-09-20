from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from bitarif_user.models import BitarifUser
from blog.models import Blog
from .serializers import BlogSerializer

from const import *


class BlogListView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


@api_view(['POST'])
def create_blog(request):
    try:
        firebase_id = request.data['firebase_id']
        title = request.data['title']
        desc = request.data['desc']
        image_link = request.data['image_link']
        text = request.data['text']

        user = BitarifUser.objects.get(firebase_id=firebase_id)
        blog = Blog.objects.create(author=user, title=title, text=text, image_link=image_link, desc=desc)
        serialized_object = BlogSerializer(blog)
        return JsonResponse({"success": True, "data": serialized_object.data})

    except BitarifUser.DoesNotExist:
        return JsonResponse({"success": False, "message": USER_NOT_FOUND_TEXT})
    except IndexError:
        return JsonResponse({"success": False, "message": MISSING_PARAMS})
    except:
        return JsonResponse({"success": False, "message": SOMETHING_WENT_WRONG})
