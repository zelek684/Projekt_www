from django.contrib import admin
from .models import Film
from .models import Osoba
from .models import Gatunek
from .models import recenzja

# Register your models here.

# @admin.register(Film)
# class filmAdmin(admin.ModelAdmin):
#     fields = ["tytul", "rokProdukcji","opis","filmwebRating","obraz","czas_trwania","rezyser","po_premierze",'Gatunek']

# @admin.register(Osoba)
# class osobaAdmin(admin.ModelAdmin):
#     fields = ["imie"]
admin.site.register(Film)
admin.site.register(Osoba)
admin.site.register(Gatunek)
admin.site.register(recenzja)


