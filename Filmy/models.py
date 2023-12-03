from django.db import models
import datetime

# Create your models here.

class Gatunek(models.Model):
    Gatunki = {
        (0, 'Horror'),
        (1, 'Dramat'),
        (2, 'Fantazy'),
        (3, 'Komedia'),
        (4, 'SCI-FI'),
        (5, 'Kryminał'),
        (6, 'Wojenny'),
        (7, 'Inne'),
    }
    gatunek_filmu = models.IntegerField(choices=Gatunki, default=7)

    class Meta:
        verbose_name_plural = "Gatunek Filmu"


    def __str__(self):
        # Sprawdzenie, czy istnieje film powiązany z gatunkiem
        if hasattr(self, 'film'):
            return f"{self.get_gatunek_filmu_display()} - {self.film.tytul}"
        return self.get_gatunek_filmu_display()


class Film(models.Model):
    tytul = models.CharField(max_length=70, blank=False, unique=True)
    rokProdukcji = models.PositiveSmallIntegerField(default=2023)
    opis = models.TextField(max_length=256,default="")
    filmwebRating = models.DecimalField(max_digits=4, decimal_places=2,null=True,blank=True,default=None)
    po_premierze = models.BooleanField(default=False)
    premiera = models.DateField(null=True, blank=True)
    obraz = models.ImageField(upload_to="obrazy", null=True,blank=True)
    czas_trwania = models.PositiveIntegerField(help_text="Czas trwania w minutach",null=True,blank=True,default=None)
    rezyser = models.ForeignKey('Osoba', on_delete=models.SET_NULL, null=True, related_name='rezyserowane_filmy')
    # obsada = models.ManyToManyField('Osoba', related_name='filmy',null=True)
    Gatunki = models.OneToOneField(Gatunek, on_delete=models.CASCADE,null=True,blank=True,related_name='film')
    class Meta:
        verbose_name_plural = "Filmy"
    def __str__(self):
        return self.tytul + "(" + str(self.rokProdukcji) + ")"


class Osoba(models.Model):
    imie = models.CharField(max_length=40,blank=False,unique=False)
    nazwisko = models.CharField(max_length=70, blank=False, unique=False)
    data_urodzenia = models.DateField(default=datetime.date(2000, 1, 1))
    opis = models.TextField(default="")
    film_many_to_many = models.ManyToManyField(Film)



    class Meta:
        verbose_name_plural = "Osoba-Aktor"

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

class recenzja(models.Model):
    opis_recenzja = models.TextField(default='nie ma')
    gwiazdka = models.IntegerField(default=1)
    many_to_one_film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='recenzja')
    class Meta:
        verbose_name_plural = "Recenzja Filmu"

    def __str__(self):
        return f"Recenzja filmu: {self.many_to_one_film.tytul}"