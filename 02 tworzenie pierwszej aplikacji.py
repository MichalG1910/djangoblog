
# 1. (myvenv) micha@micha-GF63-Thin-10UC:~/djangoblog$ python manage.py startapp blog     tworzymy nową aplikację
# 2. dodajemy naszą aplikację do pliku settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',                                     # nasza dodana aplikacja
]

# 3. w katalogu /blog dodajemy do pliku models.py

from django.db import models
from django.utils import timezone
# klasa dla naszych postów
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # autor
    title = models.CharField(max_length=200)                          # tytuł, Charfield - pole daje możliwośc wpisania 200 znaków
    text = models.TextField()                                         # pole tekstu
    created_date = models.DateTimeField(default=timezone.now)         # pole z wczytaną aktualną datą i godziną 
    publish_date = models.DateTimeField(blank=True, null=True)        # data publikacji (może byc pusta, wtedy np. artykuł będzie czekał na publikację)

    def publish(self):                                                # funkcja do publikacji artykułu
        self.publish_date = timezone.now()                            # zrobi to tylko wtedy gdy self.publish_date = timezone.now()
        self.save()                                                   # zapisanie artykulu

    def __str__(self):                                                # zwraca wlaściwość title zamieni na string i przekaże do klasy, która zapisze ją do bazy
        return self.title

# 4. przechodzimy do terminala
#    (myvenv) micha@micha-GF63-Thin-10UC:~/djangoblog$ python manage.py makemigrations blog      tworzymy migrację naszego modelu do bazy danych
'''
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post                     # dostajemy informacje o stworzeniu nowego modelu (odpowiednik modułu)
'''
# 5. (myvenv) micha@micha-GF63-Thin-10UC:~/djangoblog$ python manage.py migrate blog         dokonujemy migracji modelu do bazy danych

'''
Operations to perform:
  Apply all migrations: blog
Running migrations:
  Applying blog.0001_initial... OK
'''

# 6. /blog/admin.py   -  wchodzimy i modyfikujemy plik administracyjny

from django.contrib import admin
from .models import Post

admin.site.register(Post)               # rejestrujemy nasz model Post

# 7. po operacjijak wyżej możemy uruchomić nasz projekt na serwerze
#     (myvenv) micha@micha-GF63-Thin-10UC:~/djangoblog$ python manage.py runserver
# 8. (w chrome) 127.0.0.1:8000/admin   -   przechodzimy do panelu administracji django 
#     Prosi nas o podanie użytkownika i hasła (których nie mamy). Musimy je utworzyć
#     - zatrzymujemy w terminalu nasz projekt(ctrl + C)  
# 9. (myvenv) micha@micha-GF63-Thin-10UC:~/djangoblog$ python manage.py createsuperuser   -   tworzymy użytkownika(administratora)

'''
Nazwa użytkownika (leave blank to use 'micha'): bioly1910
Adres e-mail: grabarzmichal@gmail.com
Password: 
Password (again): 
Hasło jest zbyt podobne do nazwa użytkownika.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
'''
# 10.(myvenv) micha@micha-GF63-Thin-10UC:~/djangoblog$ python manage.py runserver

###################### pythonanywhere.com ##############################################

# wrzucanie djangoblog na chmurę pythonanwhere.com
# pythonanywhere.com/dashboard--> bash console
#w konsoli:
# pip install --user pythonanywhere  -  instalacja pythona w chmurze
# pa_autoconfigure_django.py https://github.com/bioly1910/venv.git  -  wrzucanie naszego bloga i tworzenie środowiska wirtualnego w chmurze
# python manage.py createsuperuser  -  tworzymy użytkownika(administratora) w naszej chmurze

'''
Nazwa użytkownika (leave blank to use 'micha'): bioly1910
Adres e-mail: grabarzmichal@gmail.com
Password: 
Password (again): 
Hasło jest zbyt podobne do nazwa użytkownika.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
'''
# https://bioly1910.pythonanywhere.com - adres naszej strony

# Aktualizacja naszej strony w chmurze:
'''
1. otwórz bash console
2. ls - wyświetli listę katalogów
3. cd bioly1910.pythonanywhere.com - wchodzimy do katalogu z naszą stroną
4. git pull  -  pobierze wszystkie zmiany naszej strony z naszego repezytorium Git
5. przejdź z bash console do zakładki Web
6. Reload bioly1910.pythonanywhere.com

''' 



####################### interaktywna konsola Django <QuerySet> ###################################

# (myvenv) C:\Users\mgrabarz3\pythonMain\Djangoblog>python manage.py shell                (praca) otwieramy konsolę zintegrowaną z naszym środowiskiem wirtualnym

# WAŻNE po każdym otwarciu konsoli musimy od nowa wykonywać importy, tworzyć zmienne
'''
#1# Import postów z naszego bloga


1.  >>> from blog.models import Post
2.  >>> Post.objects.all()
    <QuerySet [<Post: 1 post>]>               Wynik: otrzymamy listę wszystkich obiektow w naszym modelu Post (w tym przypadku listę postów)
'''

'''
#2# Dopisanie posta do naszego bloga

1.  >>> from django.contrib.auth.models import User
2.  >>> Users.objects.all()
    <QuerySet [<User: bioly1910>, <User: Adam>]>               Wynik: otrzymamy listę wszystkich użytkowników w modelu User 
3.  me = User.objects.get(username= 'Adam')                    Przypisujemy zmienną me do naszego użytkownika Adam
4.  >>> from blog.models import Post
5.  >>> Post.objects.create(author=me, title='Testowy wpis 2', text='Kolejna zawartość testowego wpisu') # tworzymy post
<Post: Testowy wpis 2>
6.  >>> Post.objects.all()
<QuerySet [<Post: Testowy wpis>, <Post: Testowy wpis 2>]>
'''

'''
#3# filtrowanie postów (to samo uruchomienie konsoli co wyżej, mamy już importy i zmienną me)

1.  >>> Post.objects.filter(author=me)                          # filtrujemy po autorze postu
<QuerySet [<Post: Testowy wpis>, <Post: Testowy wpis 2>]>

2.  >>> Post.objects.filter(title__contains='wpis')             # filtrujemy po tytul zawiera słowo 'wpis'
<QuerySet [<Post: Testowy wpis>, <Post: Testowy wpis 2>]>

3. >>> from django.utils import timezone
   >>> Post.objects.filter(publish_date__lte=timezone.now())    # filtrujemy po dacie publikacji(posty tworzone w <QuerySet> jej nie mają, więc ich nie wyświetli)
<QuerySet [<Post: Wpis z datą publikacji>]>

4.  >>> post = Post.objects.get(title='Testowy wpis')           # pobieramy do zmiennej post wpis o tytule= 'Testowy Wpis' (nie ma on publish_date)
>>> post.publish()                                              # publikujemy go
>>> Post.objects.filter(publish_date__lte=timezone.now())
<QuerySet [<Post: Testowy wpis>, <Post: Wpis z datą publikacji>]> # jak widać teraz filtracja po dacie publikacji zwraca nam 2 posty

'''

'''
#4# sortowanie postów 

>>> Post.objects.order_by('created_date')                                                 # sortujemy po dacie utworzenia 
<QuerySet [<Post: Testowy wpis>, <Post: Testowy wpis 2>, <Post: Wpis z datą publikacji>]>
>>> Post.objects.order_by('-created_date')                                                # odwrotne sortowanie
<QuerySet [<Post: Wpis z datą publikacji>, <Post: Testowy wpis 2>, <Post: Testowy wpis>]>
'''

'''
#5# łączenie QuerySetów

>>> Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
<QuerySet [<Post: Wpis z datą publikacji>, <Post: Testowy wpis>]>
>>> Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
<QuerySet [<Post: Testowy wpis>, <Post: Wpis z datą publikacji>]>
'''
