from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, RatingSerializer
from recommender.dispatcher import add_rating

@api_view(['POST'])
@permission_classes((AllowAny,))
def create_user(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_rating(request):
    request.data['user'] = request.user.training_id
    serialized = RatingSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        add_rating.apply_async((request.user.training_id, serialized.data['movie'], serialized.data['rating']), queue='dispatcher')
        return Response('ok', status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
