# Generated by Django 4.2.5 on 2023-10-05 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0015_surgery_immunizationhistory_familymedicalhistory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalhistoryy',
            name='current_medication',
        ),
        migrations.RemoveField(
            model_name='medicalhistoryy',
            name='previous_operation',
        ),
    ]
