# Generated by Django 3.1.1 on 2021-06-09 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210609_2312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='titel',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='paragraph',
            old_name='titel',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/title_images/'),
        ),
    ]
