# Generated by Django 3.1.1 on 2022-06-20 19:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_auto_20220620_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='url',
            field=models.CharField(default=uuid.UUID('b480c79e-4594-44a1-bbaf-a160810aeb91'), max_length=200),
        ),
    ]