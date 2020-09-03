from http import HTTPStatus

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import exceptions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from const import *
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView
from django.views.decorators.csrf import csrf_exempt

from utils import helper


@permission_classes([AllowAny])
class BitarifUserCreateView(CreateAPIView):
    serializer_class = BitarifUserCreateSerializer


class BitarifUserListView(ListAPIView):
    queryset = BitarifUser.objects.all()
    serializer_class = BitarifUserSerializer
    lookup_field = 'firebase_id'


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if email is None or password is None:
        raise exceptions.AuthenticationFailed(MISSING_PARAMS)
    try:
        user = BitarifUser.objects.get(email=email, password=password)
    except BitarifUser.DoesNotExist:
        raise exceptions.AuthenticationFailed(AUTH_FAILED)

    token = helper.generate_access_token(user.firebase_id)

    return JsonResponse({"success": True, "token": token})


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
