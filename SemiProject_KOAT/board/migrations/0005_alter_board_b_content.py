# Generated by Django 5.1.3 on 2024-12-03 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_board_b_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='b_content',
            field=models.TextField(),
        ),
    ]
