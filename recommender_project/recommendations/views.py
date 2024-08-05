from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Item, UserPreference
from .serializers import UserSerializer, ItemSerializer, UserPreferenceSerializer
from .recommender import get_recommendations

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class UserPreferenceViewSet(viewsets.ModelViewSet):
    queryset = UserPreference.objects.all()
    serializer_class = UserPreferenceSerializer

@api_view(['GET'])
def recommend(request, user_id):
    recommended_item_ids = get_recommendations(user_id)
    recommended_items = Item.objects.filter(id__in=recommended_item_ids)
    serializer = ItemSerializer(recommended_items, many=True)
    return Response(serializer.data)
