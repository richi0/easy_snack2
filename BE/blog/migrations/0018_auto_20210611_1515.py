# Generated by Django 3.1.1 on 2021-06-11 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20210611_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='city',
        ),
        migrations.RemoveField(
            model_name='article',
            name='country',
        ),
    ]