# Generated by Django 5.1.3 on 2024-12-16 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location_inform',
            name='l_like_members',
            field=models.ManyToManyField(default='', related_name='location_like_member', to='member.member'),
        ),
    ]
