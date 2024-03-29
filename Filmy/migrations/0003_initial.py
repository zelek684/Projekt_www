# Generated by Django 4.2.7 on 2023-11-27 17:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Filmy', '0002_remove_gatunek_filmy_delete_film_delete_gatunek_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=70, unique=True)),
                ('rokProdukcji', models.PositiveSmallIntegerField(default=2023)),
                ('opis', models.TextField(default='', max_length=256)),
                ('filmwebRating', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=4, null=True)),
                ('obraz', models.ImageField(blank=True, null=True, upload_to='obrazy')),
                ('czas_trwania', models.PositiveIntegerField(blank=True, default=None, help_text='Czas trwania w minutach', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=40)),
                ('nazwisko', models.CharField(max_length=70)),
                ('data_urodzenia', models.DateField(default=datetime.date(2000, 1, 1))),
                ('opis', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Gatunek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50, unique=True)),
                ('filmy', models.ManyToManyField(related_name='gatunki', to='Filmy.film')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='obsada',
            field=models.ManyToManyField(related_name='filmy', to='Filmy.osoba'),
        ),
        migrations.AddField(
            model_name='film',
            name='rezyser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rezyserowane_filmy', to='Filmy.osoba'),
        ),
    ]
