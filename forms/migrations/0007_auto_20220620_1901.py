# Generated by Django 3.1.1 on 2022-06-20 19:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_auto_20220620_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='url',
            field=models.CharField(default=uuid.UUID('926b916c-69f2-47ba-9cbe-77f4d83f4f1e'), max_length=200),
        ),
    ]
