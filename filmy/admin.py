from django.contrib import admin
from .models import Film
from .models import Osoba
from .models import Gatunek

# Register your models here.

@admin.register(Film)
class filmAdmin(admin.ModelAdmin):
    fields = ["tytul", "rokProdukcji","filmwebRating"]

# @admin.register(Osoba)
# class osobaAdmin(admin.ModelAdmin):
#     fields = ["imie"]
admin.site.register(Osoba)
admin.site.register(Gatunek)
