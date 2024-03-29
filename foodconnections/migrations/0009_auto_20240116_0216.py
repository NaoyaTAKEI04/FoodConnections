# Generated by Django 3.2.23 on 2024-01-15 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodconnections', '0008_restaurant_catchphrase'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='recommend',
            field=models.BooleanField(default=False, verbose_name='おすすめ店舗'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='ruby',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ふりがな'),
        ),
    ]
