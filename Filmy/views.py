from django.contrib.auth.models import User, Group
from django.http import HttpResponseNotAllowed
from rest_framework import viewsets,filters
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import UserSerializer
from .models import Film
from .models import recenzja
from .models import Osoba
from .serializers import FilmSerializer,recenzjaSerializer,OsobaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly,DjangoModelPermissions

# from .serializers import FilmMiniSerializer
class LargeResultsSetPagination(PageNumberPagination): #https://www.django-rest-framework.org/api-guide/pagination/
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
   # permission_classes = [permissions.IsAuthenticated]

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter,filters.OrderingFilter]
    filter_fields = ('tytul','opis','rokProdukcji')
    search_fields = ('tytul','opis')
    ordering_fields = '__all__' #http://127.0.0.1:8000/Filmy/moje_filmy/?ordering=-rokProdukcji
    ordering = ('-rokProdukcji',)  #http://127.0.0.1:8000/Filmy/moje_filmy/ automatycznie sortuje po roku
    pagination_class = LargeResultsSetPagination
    authentication_classes = (TokenAuthentication, )
    permission_classes = (DjangoModelPermissions, )   #https://www.django-rest-framework.org/api-guide/permissions/#api-reference
    #w bazie Jan_Token ma uprawnienia do dodania filmu i przegladania

    #permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        queryset = Film.objects.all()
        tytul = self.request.query_params.get('tytul', None)
        opis = self.request.query_params.get('opis', None)
        rokProdukcji = self.request.query_params.get('rokProdukcji', None)
        czas_trwania = self.request.query_params.get('czas_trwania', None)

        if tytul:
            queryset = queryset.filter(tytul__icontains=tytul)
        if opis:
            queryset = queryset.filter(opis__icontains=opis)
        if rokProdukcji:
            queryset = queryset.filter(rokProdukcji=rokProdukcji)
        if czas_trwania:
            queryset = queryset.filter(czas_trwania=czas_trwania)


        return queryset



    # def get_queryset(self):
    #     # rokProdukcji = self.request.query_params.get('rokProdukcji', None) #tu byl problem,bo po wpisaniu moje_filmy nic nie poszlo,
    #     # #dlatego zrobilam jesli np ?rokProdukcji=2000 to ok
    #     # if rokProdukcji:
    #     #     zmienna_qs = Film.objects.filter(rokProdukcji=rokProdukcji)
    #     # else: #jsli same filmy to all
    #     zmienna_qs = Film.objects.all()
    #     return zmienna_qs

    # def list(self, request, *args, **kwargs):
    #     tytul = self.request.query_params.get('tytul', None)
    #     zmienna_qs = Film.objects.filter(tytul__contains=tytul) #iexact nie rozroznia wielkosci liter
    #
    #     # queryset = self.get_queryset()
    #
    #     serializer = FilmSerializer(zmienna_qs, many=True)
    #     return Response(serializer.data)
    # obsługa ządań HTTP GET dla pojedynczego obiektu
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()  # pobiera obiekt z bazy danych na podstawie klucza przekazanego w URL
        serializer = FilmSerializer(instance) #tworze obiekt serializer, który konwertuje model obiektu (model Film)
        return Response(serializer.data)
    #dane z serializera (które są teraz w formie słownika Pythona) są przekazywane do obiektu Response. DRF zajmie się
    # konwersją tego słownika na JSON i zwróci go jako odpowiedź HTTP z odpowiednim kodem statusu (domyślnie 200 OK).
    #https://www.django-rest-framework.org/api-guide/viewsets/#viewsets



    def create(self, request, *args, **kwargs):
        #if request.user.is_superuser:  #jesli uzytkownik jest superuser to wykonam
            nowy_film = Film.objects.create(tytul=request.data['tytul'],
                                        opis=request.data['opis'],
                                        po_premierze=request.data['po_premierze'],
                                        rokProdukcji=request.data['rokProdukcji'],
                                        czas_trwania=request.data['czas_trwania'],)


            serializer = FilmSerializer(nowy_film, many=False)
            return Response(serializer.data)
        #else: #jesli nie to blad not allowed
            #return HttpResponseNotAllowed('Niedozwolony')

    def update(self, request, *args, **kwargs):
        update_film = self.get_object()
        update_film.tytul = request.data['tytul']
        update_film.opis = request.data['opis']
        update_film.po_premierze = request.data['po_premierze']
        update_film.rokProdukcji = request.data['rokProdukcji']
        update_film.czas_trwania = request.data['czas_trwania']
        update_film.save()
        serializer = FilmSerializer(update_film, many=False)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        delete_film = self.get_object()
        delete_film.delete()
        return Response('Film został usunięty')

    #http://127.0.0.1:8000/Filmy/moje_filmy/2/premiera/
    #metoda która zmienia po_premierze z False na True
    @action(detail=True)
    def premiera(self, request, **kwargs):
        premiera_film = self.get_object()
        premiera_film.po_premierze = True
        premiera_film.save()
        serializer = FilmSerializer(premiera_film, many=False)
        return Response(serializer.data)
    #testuje dla wszystkich rekordów (wszystkie filmy po_premierze z false na true)
    #http://127.0.0.1:8000/Filmy/moje_filmy/premiera_all/
    @action(detail=False, methods=['post'])
    def premiera_all(self, request, **kwargs):
        premiera_filmy_update = Film.objects.all()
        premiera_filmy_update.update(po_premierze=request.data['po_premierze'])

        serializer = FilmSerializer(premiera_filmy_update, many=True)
        return Response(serializer.data)

class recenzjaViewSet(viewsets.ModelViewSet):
    queryset = recenzja.objects.all()
    serializer_class = recenzjaSerializer

class OsobaViewSet(viewsets.ModelViewSet):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer

    @action(detail=True, methods=['post'])
    def polaczAktoraZfilmem(self, request, **kwargs):
        osoba = self.get_object()
        film = Film.objects.get(id=request.data['film'])
        osoba.film_many_to_many.add(film)
        serializer = OsobaSerializer(osoba, many=False)
        return Response(serializer.data)



    










