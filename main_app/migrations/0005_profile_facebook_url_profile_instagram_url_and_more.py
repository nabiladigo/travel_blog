# Generated by Django 4.0.2 on 2022-10-21 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_url',
            field=models.CharField(default='last name', max_length=225),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(default='last name', max_length=225),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_url',
            field=models.CharField(default='last name', max_length=225),
        ),
        migrations.AddField(
            model_name='profile',
            name='website_url',
            field=models.CharField(default='last name', max_length=225),
        ),
    ]