# Generated by Django 2.1.7 on 2019-03-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20190313_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=200, unique=True)),
        ),
    ]
