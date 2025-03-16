from django.contrib import admin
from .models import Advertiser, AdCampaign, AdSlot, Ad, Impression, Click

@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email')
    search_fields = ('name', 'contact_email')
    verbose_name = "Рекламодатель"
    verbose_name_plural = "Рекламодатели"

@admin.register(AdCampaign)
class AdCampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'advertiser', 'start_date', 'end_date')
    search_fields = ('name', 'advertiser__name')
    list_filter = ('start_date', 'end_date')
    verbose_name = "Рекламная кампания"
    verbose_name_plural = "Рекламные кампании"

@admin.register(AdSlot)
class AdSlotAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    verbose_name = "Рекламный слот"
    verbose_name_plural = "Рекламные слоты"

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'slot', 'target_url', 'is_active')
    list_filter = ('campaign', 'slot', 'is_active')
    search_fields = ('campaign__name', 'slot__name', 'target_url')
    verbose_name = "Реклама"
    verbose_name_plural = "Рекламные объявления"

@admin.register(Impression)
class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('ad', 'timestamp')
    search_fields = ('ad__campaign__name', 'timestamp')
    list_filter = ('timestamp',)
    verbose_name = "Показ рекламы"
    verbose_name_plural = "Показы рекламы"

@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ('ad', 'timestamp')
    search_fields = ('ad__campaign__name', 'timestamp')
    list_filter = ('timestamp',)
    verbose_name = "Клик по рекламе"
    verbose_name_plural = "Клики по рекламе"
