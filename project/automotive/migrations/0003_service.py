# Generated by Django 3.2.7 on 2021-10-06 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automotive', '0002_advisor_dealership'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_date', models.DateField()),
                ('link', models.TextField()),
                ('service', models.TextField()),
                ('mileage', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('comments', models.TextField()),
                ('inserted_date', models.DateTimeField()),
                ('dealership', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='automotive.dealership')),
                ('make', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='automotive.vehicle')),
                ('service_advisor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='automotive.advisor')),
            ],
        ),
    ]
