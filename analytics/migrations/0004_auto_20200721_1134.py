# Generated by Django 3.0.7 on 2020-07-21 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_auto_20200721_1105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clickevent',
            old_name='Kirr_url',
            new_name='kirr_url',
        ),
    ]