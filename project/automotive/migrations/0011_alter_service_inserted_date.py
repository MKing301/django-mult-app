# Generated by Django 3.2.7 on 2021-10-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automotive', '0010_auto_20211014_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='inserted_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]