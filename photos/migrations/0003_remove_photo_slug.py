# Generated by Django 2.1.7 on 2019-03-13 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_photo_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='slug',
        ),
    ]
