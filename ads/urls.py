from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvertiserViewSet, AdCampaignViewSet, AdSlotViewSet, AdViewSet, ImpressionViewSet, ClickViewSet

router = DefaultRouter()
router.register(r'advertisers', AdvertiserViewSet)
router.register(r'campaigns', AdCampaignViewSet)
router.register(r'slots', AdSlotViewSet)
router.register(r'ads', AdViewSet)
router.register(r'impressions', ImpressionViewSet)
router.register(r'clicks', ClickViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
