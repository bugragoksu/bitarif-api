import datetime
import jwt
from django.conf import settings


def generate_access_token(firebase_id):
    access_token_payload = {
        'firebase_id': firebase_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload,
                              settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
    return access_token
