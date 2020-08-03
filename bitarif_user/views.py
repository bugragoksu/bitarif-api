from http import HTTPStatus

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from const import *
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class BitarifUserCreateView(CreateAPIView):
    serializer_class = BitarifUserCreateSerializer


class BitarifUserListView(ListAPIView):
    queryset = BitarifUser.objects.all()
    serializer_class = BitarifUserSerializer
    lookup_field = 'firebase_id'


@csrf_exempt
@api_view(['POST'])
def add_user_follower(request):
    try:
        following_user_id = request.data['following_user_id']
        followed_user_id = request.data['followed_user_id']
    except:
        return HttpResponse(status=HTTPStatus.BAD_REQUEST)

    try:
        following_user = BitarifUser.objects.get(firebase_id=following_user_id)
        followed_user = BitarifUser.objects.get(firebase_id=followed_user_id)
    except BitarifUser.DoesNotExist:
        return JsonResponse({"success": False, "message": USER_NOT_FOUND_TEXT})
    try:
        followed_user.follower.add(following_user)
        followed_user.save()
        return JsonResponse({"success": True, "message": SUCCESSFUL_TEXT})
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)})
