# Generated by Django 4.2.6 on 2023-10-22 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0008_film_rezyser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gatunek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]