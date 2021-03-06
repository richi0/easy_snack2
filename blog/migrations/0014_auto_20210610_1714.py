# Generated by Django 3.1.1 on 2021-06-10 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210610_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='city',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='cost',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='article',
            name='country',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='', upload_to='uploads/title_images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='preface',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='restaurant_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
