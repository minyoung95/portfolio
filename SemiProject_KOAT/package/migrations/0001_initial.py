# Generated by Django 5.1.3 on 2025-01-03 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('p_no', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=100)),
                ('p_price', models.IntegerField()),
                ('p_file', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
