# Generated by Django 4.2.5 on 2023-09-28 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0008_rename_age_patient_age_years'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalhistoryy',
            name='age',
        ),
        migrations.AddField(
            model_name='medicalhistoryy',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='medicalhistoryy',
            name='age_years',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='medicalhistoryy',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='medicalhistoryy',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
