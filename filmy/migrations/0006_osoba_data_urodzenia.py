# Generated by Django 4.2.6 on 2023-10-22 22:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0005_osoba_opis_alter_film_filmwebrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='data_urodzenia',
            field=models.DateField(default=datetime.date(2000, 1, 1)),
        ),
    ]