# Generated by Django 3.1.1 on 2021-06-11 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20210610_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='uploads/countries/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='uploads/places/')),
                ('description', models.TextField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.country')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='city_link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.city'),
        ),
        migrations.AddField(
            model_name='article',
            name='country_link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.country'),
        ),
    ]
