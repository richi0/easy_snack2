# Generated by Django 3.1.1 on 2021-06-07 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210607_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='restaurant_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
