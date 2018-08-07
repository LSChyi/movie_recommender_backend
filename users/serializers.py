from rest_framework import serializers
from .models import User, Rating

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('user', 'movie', 'rating')
