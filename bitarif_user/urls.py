from django.urls import path
from .views import *

urlpatterns = [
    path('list/', BitarifUserListView.as_view(), name='User List'),
    path('create/', BitarifUserCreateView.as_view(), name='User Create'),
    path('add_follower/', add_user_follower, name='Add Follower'),
    path('login/', login_view, name='Login'),
    path('get-follows-by-user/', get_follows_by_user, name='Get follows by user'),

]
