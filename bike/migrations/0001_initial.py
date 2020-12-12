# Generated by Django 3.1.2 on 2020-12-12 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike_type', models.CharField(choices=[('Road', 'Road'), ('Hybrid', 'Hybrid'), ('Mountain', 'Mountain'), ('BMX', 'BMX'), ('Childrens', 'Childrens'), ('Other', 'Other')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='FrameType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_type', models.CharField(choices=[('Carbon Fiber', 'Carbon Fiber'), ('Steel', 'Steel'), ('Titanium', 'Titanium'), ('Aluminum', 'Aluminum'), ('Other', 'Other')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='HandlebarType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handlebar_type', models.CharField(choices=[('Flat', 'Flat'), ('Riser', 'Riser'), ('Drop', 'Drop'), ('Bullhorn', 'Bullhorn'), ('Aero', 'Aero'), ('Cruiser', 'Cruiser'), ('Butterfly', 'Butterfly'), ('Other', 'Other')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_size', models.CharField(choices=[('XX Small', 'XX Small'), ('X Small', 'X Small'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('X Large', 'X Large'), ('XX Large', 'XX Large'), ('XXX Large', 'XXX Large')], default='Small', max_length=15)),
                ('owner_description', models.TextField()),
                ('age', models.IntegerField(default=0)),
                ('current', models.BooleanField(default=True)),
                ('bike_creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('bike_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike.biketype')),
                ('frame_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike.frametype')),
                ('handlebar_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike.handlebartype')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Bikes',
            },
        ),
    ]
