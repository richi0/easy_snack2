# Generated by Django 3.1.1 on 2021-06-07 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210607_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='stars',
            field=models.FloatField(choices=[(0, 0), (0.5, 0.5), (1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5)], default=0),
        ),
    ]
