# Generated by Django 4.1.13 on 2023-12-01 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Filmy', '0011_alter_gatunek_gatunek_filmu_recenzja'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recenzja',
            options={'verbose_name_plural': 'Recenzja Filmu'},
        ),
        migrations.AlterField(
            model_name='gatunek',
            name='gatunek_filmu',
            field=models.IntegerField(choices=[(2, 'Fantazy'), (3, 'Komedia'), (4, 'SCI-FI'), (5, 'Kryminał'), (1, 'Dramat'), (0, 'Horror'), (6, 'Wojenny'), (7, 'Inne')], default=7),
        ),
    ]
