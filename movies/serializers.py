from rest_framework import serializers
from .models import Movie, MovieTrailer

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'poster_partial_url')

class MovieTrailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieTrailer
        fields = ('youtube_id',)
