# Generated by Django 4.2.6 on 2023-10-22 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0009_gatunek'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='obsada',
            field=models.ManyToManyField(related_name='filmy', to='filmy.osoba'),
        ),
        migrations.AddField(
            model_name='gatunek',
            name='filmy',
            field=models.ManyToManyField(related_name='gatunki', to='filmy.film'),
        ),
    ]