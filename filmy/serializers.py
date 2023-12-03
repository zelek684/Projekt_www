from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Film, Gatunek, recenzja,Osoba


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email','password']
        write_only = {'password': {'required': True, 'write_only':True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
class GatunekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gatunek
        fields = ['gatunek_filmu']
class recenzjaSerializer(serializers.ModelSerializer):

    class Meta:
        model = recenzja
        fields = '__all__'
        #depth = 1
        #exklude

    def update(self, instance, validated_data):  # zapisuje PUT tylko recencje i gwiazdka many_to_one_film nie bo to bez sensu jest
        instance.opis_recenzja = validated_data.get('opis_recenzja',instance.opis_recenzja)
        instance.gwiazdka = validated_data.get('gwiazdka',instance.gwiazdka)
        instance.save()

        return instance



class FilmSerializer(serializers.ModelSerializer):
    Gatunki = GatunekSerializer(many=False)
    recenzja = recenzjaSerializer(many=True)
    class Meta:
        model = Film
        fields = ['id','tytul', 'rokProdukcji', 'opis', 'filmwebRating','po_premierze','premiera','obraz','czas_trwania','rezyser','Gatunki','recenzja']
        read_only_fields = ('Gatunki','recencja')  #wyswietlam tylko




class FilmMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['tytul', 'rokProdukcji',]

class OsobaSerializer(serializers.ModelSerializer):
    film_many_to_many = FilmMiniSerializer(many =True,read_only=True)
    class Meta:
        model = Osoba
        fields = ['id','imie','nazwisko','data_urodzenia','opis','film_many_to_many']

    # def create(self, validated_data):
    #     film_many_to_many = validated_data["film_many_to_many"]
    #     del validated_data["film_many_to_many"]
    #
    #     osoba_aktor = Osoba.objects.create(**validated_data)
    #     for film in film_many_to_many:
    #         i = Film.objects.create(**film)
    #         osoba_aktor.film_many_to_many.add(i)
    #
    #     osoba_aktor.save()
    #     return osoba_aktor

