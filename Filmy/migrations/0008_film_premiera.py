# Generated by Django 4.1.13 on 2023-12-01 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Filmy', '0007_alter_film_options_alter_gatunek_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='premiera',
            field=models.DateField(blank=True, null=True),
        ),
    ]
