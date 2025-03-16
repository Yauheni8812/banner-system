from django.db import models
from django.contrib.auth.models import AbstractUser

# Кастомный пользователь
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('advertiser', 'Рекламодатель'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='advertiser')

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="ads_users",  # Исправляем конфликт имен
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="ads_users_permissions",  # Исправляем конфликт имен
        blank=True
    )

# Рекламодатель
class Advertiser(models.Model):
    name = models.CharField(max_length=255, unique=True)
    contact_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рекламодатель"
        verbose_name_plural = "Рекламодатели"

# Рекламная кампания
class AdCampaign(models.Model):
    name = models.CharField(max_length=255)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рекламная кампания"
        verbose_name_plural = "Рекламные кампании"

# Место размещения рекламы (рекламный блок)
class AdSlot(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рекламный слот"
        verbose_name_plural = "Рекламные слоты"

# Рекламное объявление
class Ad(models.Model):
    campaign = models.ForeignKey(AdCampaign, on_delete=models.CASCADE)
    slot = models.ForeignKey(AdSlot, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ads/')
    target_url = models.URLField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.campaign.name} - {self.slot.name}"

    class Meta:
        verbose_name = "Рекламное объявление"
        verbose_name_plural = "Рекламные объявления"

# Фиксация показа рекламы
class Impression(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Показ рекламы"
        verbose_name_plural = "Показы рекламы"

# Фиксация клика по рекламе
class Click(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Клик по рекламе"
        verbose_name_plural = "Клики по рекламе"
