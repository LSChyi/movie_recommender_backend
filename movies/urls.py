from django.urls import include, path
from .views import get_recommendations, get_trailers

urlpatterns = [
    path('recommendations/', get_recommendations),
    path('<int:movie_id>/trailers/', get_trailers),
]
