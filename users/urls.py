from django.urls import include, path
from .views import create_user, create_rating

urlpatterns = [
    path('register/', create_user),
    path('ratings/', create_rating)
]
