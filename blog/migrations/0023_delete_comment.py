# Generated by Django 3.1.1 on 2021-06-17 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_article_caption'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
