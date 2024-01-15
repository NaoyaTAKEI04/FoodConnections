# Generated by Django 3.2.23 on 2024-01-15 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodconnections', '0004_auto_20240115_1357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='auther',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='カテゴリー'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(max_length=100, verbose_name='住所'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='foodconnections.category', verbose_name='カテゴリー'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='restaurant_images/', verbose_name='画像'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=100, verbose_name='店名'),
        ),
    ]