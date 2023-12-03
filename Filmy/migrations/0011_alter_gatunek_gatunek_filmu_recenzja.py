# Generated by Django 4.1.13 on 2023-12-01 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Filmy', '0010_rename_wybierz_gatunek_film_gatunki_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatunek',
            name='gatunek_filmu',
            field=models.IntegerField(choices=[(1, 'Dramat'), (7, 'Inne'), (4, 'SCI-FI'), (5, 'Kryminał'), (2, 'Fantazy'), (3, 'Komedia'), (0, 'Horror'), (6, 'Wojenny')], default=7),
        ),
        migrations.CreateModel(
            name='recenzja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opis_recenzja', models.TextField(default='nie ma')),
                ('gwiazdka', models.IntegerField(default=1)),
                ('many_to_one_film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Filmy.film')),
            ],
        ),
    ]
