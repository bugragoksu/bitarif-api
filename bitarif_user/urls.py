from django.urls import path
from .views import *

urlpatterns = [
    path('list/', BitarifUserListView.as_view(), name='User List'),

]
