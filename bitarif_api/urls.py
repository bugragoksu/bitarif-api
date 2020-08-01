from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/recipe/', include('recipe.urls')),
    path('api/user/', include('bitarif_user.urls')),
]
