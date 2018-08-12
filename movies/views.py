from random import sample
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Movie, MovieTrailer
from users.models import Rating
from .serializers import MovieSerializer, MovieTrailerSerializer
from recommender.dispatcher import recommend

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_recommendations(request):
    if Rating.objects.filter(user=request.user).exists():
        selected_ids = recommend.apply_async((request.user.training_id,), queue='dispatcher').get()
        rated = Rating.objects.filter(user=request.user, movie__in=selected_ids)
        for rating in rated:
            if rating.movie.id in selected_ids:
                selected_ids.remove(rating.movie.id)
        selected_ids = selected_ids[:10]
    else:
        movie_num = Movie.objects.all().count()
        selected_ids = sample(range(movie_num), 10)
    movies = Movie.objects.filter(id__in=selected_ids)
    serialized = MovieSerializer(movies, many=True)
    return Response(serialized.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((AllowAny,))
def get_trailers(request, movie_id):
    trailers = MovieTrailer.objects.filter(movie__id = movie_id)
    serialized = MovieTrailerSerializer(trailers, many=True)
    return Response(serialized.data, status=status.HTTP_200_OK)
