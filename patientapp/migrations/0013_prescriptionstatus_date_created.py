# Generated by Django 4.2.5 on 2023-10-03 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0012_card_description2'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescriptionstatus',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]