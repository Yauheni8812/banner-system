from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Advertiser, AdCampaign, AdSlot, Ad, Impression, Click
from .serializers import AdvertiserSerializer, AdCampaignSerializer, AdSlotSerializer, AdSerializer, ImpressionSerializer, ClickSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class AdvertiserViewSet(viewsets.ModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer

class AdCampaignViewSet(viewsets.ModelViewSet):
    queryset = AdCampaign.objects.all()
    serializer_class = AdCampaignSerializer

class AdSlotViewSet(viewsets.ModelViewSet):
    queryset = AdSlot.objects.all()
    serializer_class = AdSlotSerializer

    # Пагинация (10 баннеров на страницу)
class AdPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

from rest_framework.permissions import IsAuthenticated  # 🔹 Добавили импорт

class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['is_active', 'campaign__advertiser']
    ordering_fields = ['campaign__name', 'slot__name', 'is_active']
    
    # 🔐 Требуем авторизацию!
    permission_classes = [IsAuthenticated]



class ImpressionViewSet(viewsets.ModelViewSet):
    queryset = Impression.objects.all()
    serializer_class = ImpressionSerializer

class ClickViewSet(viewsets.ModelViewSet):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer
