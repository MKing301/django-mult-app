# Generated by Django 3.2.7 on 2021-10-05 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=25)),
                ('year', models.CharField(max_length=4)),
                ('vin', models.CharField(max_length=17)),
                ('license_plate', models.CharField(max_length=8)),
                ('color', models.CharField(max_length=15)),
            ],
        ),
    ]
