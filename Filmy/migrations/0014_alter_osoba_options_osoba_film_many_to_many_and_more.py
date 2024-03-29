# Generated by Django 4.1.13 on 2023-12-01 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Filmy', '0013_alter_gatunek_gatunek_filmu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'verbose_name_plural': 'Osoba-Aktor'},
        ),
        migrations.AddField(
            model_name='osoba',
            name='film_many_to_many',
            field=models.ManyToManyField(to='Filmy.film'),
        ),
        migrations.AlterField(
            model_name='gatunek',
            name='gatunek_filmu',
            field=models.IntegerField(choices=[(2, 'Fantazy'), (0, 'Horror'), (6, 'Wojenny'), (4, 'SCI-FI'), (1, 'Dramat'), (7, 'Inne'), (3, 'Komedia'), (5, 'Kryminał')], default=7),
        ),
        migrations.AlterField(
            model_name='recenzja',
            name='many_to_one_film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recenzja', to='Filmy.film'),
        ),
    ]
