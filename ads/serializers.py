from rest_framework import serializers
from .models import Advertiser, AdCampaign, AdSlot, Ad, Impression, Click

class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = '__all__'

class AdCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdCampaign
        fields = '__all__'

class AdSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdSlot
        fields = '__all__'

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
        extra_kwargs = {
            'campaign': {'label': 'Кампания'},
            'slot': {'label': 'Рекламный слот'},
            'image': {'label': 'Изображение'},
            'target_url': {'label': 'Целевая ссылка'},
            'is_active': {'label': 'Активно'},
        }

class ImpressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impression
        fields = '__all__'

class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = '__all__'
