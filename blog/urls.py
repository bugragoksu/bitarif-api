from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('list/', BlogListView.as_view(), name='Blog List'),
    path('create/', create_blog, name='Blog Create'),
    path('get-liked-blogs/', get_liked_blogs, name='Get liked blog'),
]
