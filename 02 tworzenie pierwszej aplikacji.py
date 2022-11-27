
# 1. (myvenv) micha@micha-GF63-Thin-10UC:~/venv$ python manage.py startapp blog     tworzymy nową aplikację
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
#    (myvenv) micha@micha-GF63-Thin-10UC:~/venv$ python manage.py makemigrations blog      tworzymy migrację naszego modelu do bazy danych
'''
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post                     # dostajemy informacje o stworzeniu nowego modelu (odpowiednik modułu)
'''
# 5. (myvenv) micha@micha-GF63-Thin-10UC:~/venv$ python manage.py migrate blog         dokonujemy migracji modelu do bazy danych

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
#     (myvenv) micha@micha-GF63-Thin-10UC:~/venv$ python manage.py runserver
# 8. (w chrome) 127.0.0.1:8000/admin   -   przechodzimy do panelu administracji django 
#     Prosi nas o podanie użytkownika i hasła (których nie mamy). Musimy je utworzyć
#     - zatrzymujemy w terminalu nasz projekt(ctrl + C)  
# 9. (myvenv) micha@micha-GF63-Thin-10UC:~/venv$ python manage.py createsuperuser   -   tworzymy użytkownika(administratora)

'''
Nazwa użytkownika (leave blank to use 'micha'): bioly1910
Adres e-mail: grabarzmichal@gmail.com
Password: 
Password (again): 
Hasło jest zbyt podobne do nazwa użytkownika.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
'''
# 10.(myvenv) micha@micha-GF63-Thin-10UC:~/venv$ python manage.py runserver

