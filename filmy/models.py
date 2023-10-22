from django.db import models
import datetime

# Create your models here.


class Film(models.Model):
    tytul = models.CharField(max_length=70, blank=False, unique=True)
    rokProdukcji = models.PositiveSmallIntegerField(default=2023)
    opis = models.TextField(default="")
    filmwebRating = models.DecimalField(max_digits=4, decimal_places=2,null=True,blank=True,default=None)
    obraz = models.ImageField(upload_to="obrazy", null=True,blank=True)
    czas_trwania = models.PositiveIntegerField(help_text="Czas trwania w minutach",null=True,blank=True,default=None)
    rezyser = models.ForeignKey('Osoba', on_delete=models.SET_NULL, null=True, related_name='rezyserowane_filmy')
    obsada = models.ManyToManyField('Osoba', related_name='filmy')

class Gatunek(models.Model):
    nazwa = models.CharField(max_length=50, unique=True)
    filmy = models.ManyToManyField(Film, related_name='gatunki')

    def __str__(self):
        return self.nazwa
class Osoba(models.Model):
    imie = models.CharField(max_length=40,blank=False,unique=False)
    nazwisko = models.CharField(max_length=70, blank=False, unique=False)
    data_urodzenia = models.DateField(default=datetime.date(2000, 1, 1))
    opis = models.TextField(default="")


    def __str__(self):
        return self.tytul