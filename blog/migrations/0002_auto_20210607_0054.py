# Generated by Django 3.1.1 on 2021-06-07 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='city',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='cost',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='country',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='position',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='restaurant_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='stars',
            field=models.IntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default=1),
        ),
    ]