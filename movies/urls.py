from django.urls import include, path
from .views import get_recommendations

urlpatterns = [
    path('recommendations/', get_recommendations)
]
