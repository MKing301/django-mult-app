# Generated by Django 3.2.7 on 2021-10-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automotive', '0009_auto_20211006_2155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='service',
            new_name='work_performed',
        ),
        migrations.AlterField(
            model_name='dealership',
            name='name',
            field=models.TextField(),
        ),
    ]
