# Generated by Django 3.2.7 on 2021-10-06 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automotive', '0003_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealership',
            name='_state',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='dealership',
            name='city',
            field=models.CharField(max_length=50),
        ),
    ]
