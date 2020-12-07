# Generated by Django 3.1.2 on 2020-12-06 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='bike',
        ),
        migrations.AddField(
            model_name='order',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='userprofile.userprofile'),
        ),
    ]