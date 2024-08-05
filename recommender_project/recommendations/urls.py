from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ItemViewSet, UserPreferenceViewSet, recommend

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'items', ItemViewSet)
router.register(r'preferences', UserPreferenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('recommend/<int:user_id>/', recommend),
]
