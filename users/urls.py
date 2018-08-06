from django.urls import include, path
from .views import create_user

urlpatterns = [
    path('register/', create_user),
]
