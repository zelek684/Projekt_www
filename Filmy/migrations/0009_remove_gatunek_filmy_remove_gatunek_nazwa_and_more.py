# Generated by Django 4.1.13 on 2023-12-01 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Filmy', '0008_film_premiera'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gatunek',
            name='filmy',
        ),
        migrations.RemoveField(
            model_name='gatunek',
            name='nazwa',
        ),
        migrations.AddField(
            model_name='film',
            name='wybierz_gatunek',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Filmy.gatunek'),
        ),
        migrations.AddField(
            model_name='gatunek',
            name='gatunek_filmu',
            field=models.IntegerField(choices=[(1, 'Dramat'), (4, 'SCI-FI'), (0, 'Horror'), (5, 'Kryminał'), (7, 'Inne'), (3, 'Komedia'), (2, 'Fantazy'), (6, 'Wojenny')], default=7),
        ),
    ]