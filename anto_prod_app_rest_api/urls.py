"""
URL configuration for anto_prod_app_rest_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route
from dj_rest_auth.jwt_auth import get_refresh_view

urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/token/refresh/',
         get_refresh_view().as_view(), name='token_refresh'),
    path('', include('profiles.urls')),
    path('', include('categories.urls')),
    path('', include('priorities.urls')),
    path('', include('states.urls')),
    path('', include('tasks.urls')),
    path('', include('taskstatus.urls')),
]
