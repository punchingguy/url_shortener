# Generated by Django 3.0.7 on 2020-07-21 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shortener', '0004_auto_20200718_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('Kirr_url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shortener.KirrURL')),
            ],
        ),
    ]