# Generated by Django 5.0.2 on 2024-02-28 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking',
            new_name='BookingItem',
        ),
        migrations.RenameModel(
            old_name='Menu',
            new_name='MenuItem',
        ),
    ]
