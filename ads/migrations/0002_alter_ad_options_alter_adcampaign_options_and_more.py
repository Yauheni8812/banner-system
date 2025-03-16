# Generated by Django 5.1.7 on 2025-03-16 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'verbose_name': 'Рекламное объявление', 'verbose_name_plural': 'Рекламные объявления'},
        ),
        migrations.AlterModelOptions(
            name='adcampaign',
            options={'verbose_name': 'Рекламная кампания', 'verbose_name_plural': 'Рекламные кампании'},
        ),
        migrations.AlterModelOptions(
            name='adslot',
            options={'verbose_name': 'Рекламный слот', 'verbose_name_plural': 'Рекламные слоты'},
        ),
        migrations.AlterModelOptions(
            name='advertiser',
            options={'verbose_name': 'Рекламодатель', 'verbose_name_plural': 'Рекламодатели'},
        ),
        migrations.AlterModelOptions(
            name='click',
            options={'verbose_name': 'Клик по рекламе', 'verbose_name_plural': 'Клики по рекламе'},
        ),
        migrations.AlterModelOptions(
            name='impression',
            options={'verbose_name': 'Показ рекламы', 'verbose_name_plural': 'Показы рекламы'},
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Администратор'), ('advertiser', 'Рекламодатель')], default='advertiser', max_length=20),
        ),
        migrations.DeleteModel(
            name='Campaign',
        ),
    ]
