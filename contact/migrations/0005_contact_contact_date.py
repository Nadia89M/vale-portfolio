# Generated by Django 2.1.7 on 2019-03-14 16:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_remove_contact_received_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
