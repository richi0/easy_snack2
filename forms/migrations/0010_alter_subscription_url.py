# Generated by Django 4.0.5 on 2022-06-28 18:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0009_alter_subscription_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='url',
            field=models.CharField(default=uuid.UUID('600ac7e0-4677-49fd-9a19-531b316accc3'), max_length=200),
        ),
    ]
