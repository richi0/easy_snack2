# Generated by Django 4.0.5 on 2022-07-02 19:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0010_alter_subscription_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='url',
            field=models.CharField(default=uuid.UUID('473f5ca8-e8b4-415a-8d30-9babfdc72465'), max_length=200),
        ),
    ]