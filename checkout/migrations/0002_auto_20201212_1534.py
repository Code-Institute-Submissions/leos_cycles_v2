# Generated by Django 3.1.2 on 2020-12-12 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='preferred_service_date',
            field=models.DateField(help_text='YYYY-mm-dd'),
        ),
    ]
