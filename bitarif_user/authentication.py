import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.conf import settings

from const import USER_NOT_FOUND_TEXT, AUTH_FAILED
from bitarif_user.models import BitarifUser


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):

        authorization_header = request.headers.get('Authorization')

        if not authorization_header:
            return None
        try:
            # header = 'Token xxxxxxxxxxxxxxxxxxxxxxxx'
            access_token = authorization_header.split(' ')[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')
        except:
            raise exceptions.AuthenticationFailed(AUTH_FAILED)
        try:
            user = BitarifUser.objects.get(firebase_id=payload['firebase_id'])
        except BitarifUser.DoesNotExist:
            raise exceptions.AuthenticationFailed(USER_NOT_FOUND_TEXT)


        return (user, None)