# Generated by Django 4.0.4 on 2024-03-26 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DigiCare', '0003_prescriptionform_doctorusername'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
