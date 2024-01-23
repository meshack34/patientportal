# Generated by Django 4.2.5 on 2023-10-05 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0014_rename_investgation_investigation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surgery_type', models.CharField(max_length=100)),
                ('surgery_date', models.DateField()),
                ('reason', models.CharField(max_length=200)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='ImmunizationHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_condition', models.CharField(max_length=100)),
                ('affected_member_name', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='CurrentMedication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=100)),
                ('reason', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy_name', models.CharField(max_length=100)),
                ('severity', models.CharField(max_length=50)),
                ('diagnosis_date', models.DateField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientapp.patient')),
            ],
        ),
    ]
