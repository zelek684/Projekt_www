# Generated by Django 4.2.6 on 2023-10-22 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0006_osoba_data_urodzenia'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='czas_trwania',
            field=models.PositiveIntegerField(blank=True, default=None, help_text='Czas trwania w minutach', null=True),
        ),
    ]