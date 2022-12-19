# 1. środowisko wirtualne (zwane też virtualenv).
'''
- tworzymy katalog w ktorym zainstalujemy środowisko wirtualne djangoblog
- będąc w katalogu djangoblog wpisyjemy w terminalu: (windows/linux)python -m venv myvenv/python3 -m venv myvenv        w katalogu myvenv będize zainstalowane środowisko wirtualne
- zainstaluj najnowszą wersję instalatora pip
- zainstaluj Django w będąc w uruchomionym środowisku wirtualnym (myvenv) patrz niżej 
'''
# 2. Obsługa środowiska wirtualnego i tworzenie nowego projektu
'''
Dla windows
D:\python\basics\strefakursow\06 django\djangoblog\myvenv\Scripts>activate  - uruchomienie naszego środowiska wirtualnego
D:\python\basics\strefakursow\06 django\djangoblog>django-admin startproject mysite .  - rozpoczęcie nowego projektu (wykonujemy tylko raz)
(myvenve) D:\python\basics\strefakursow\06 django\djangoblog>python manage.py migrate  - łączenie projektu z bazą danych (wykonujemy tylko raz)
(myvenve) D:\python\basics\strefakursow\06 django\djangoblog>python manage.py runserver  - uruchomienie servera naszego projektu''''''

Dla Ubuntu
cd /home/micha/venv   --->   source myvenv/bin/activate
(myvenv) micha@micha-GF63-Thin-10UC:~/djangoblog$ django-admin startproject mysite .        (wykonujemy tylko raz)
(myvenv) micha@micha-GF63-Thin-10UC:~/djangoblog$ python manage.py migrate                  (wykonujemy tylko raz)
(myvenv) micha@micha-GF63-Thin-10UC:~/djangoblog$ python manage.py runserver                
(myvenv) micha@micha-GF63-Thin-10UC:~/djangoblog$ python manage.py startapp blog            tworzymy nową aplikację

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 25, 2022 - 08:59:08
Django version 4.1.3, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/    # wklej w wyszukiwarkę aby uruchomić
Quit the server with CTRL-BREAK.        dla ubuntu: Quit the server with CONTROL-C

Zewnętrzny katalog główny mysite/       jest pojemnikiem na twój projekt. Jego nazwa nie ma znaczenia dla Django; możesz zmienić jego 
                                        nazwę na dowolną, jaką chcesz.
manage.py:                              Narzędzie linii komend, które pozwala ci oddziaływać z tym projektem Django na wiele sposobów.
                                        Możesz przeczytać szczegóły na temat manage.py w django-admin and manage.py.
Wewnętrzny katalog mysite/              jest właściwym pakietem Pythona dla twojego projektu. Jego nazwa jest nazwą pakietu Pythona, 
                                        którą musisz używać, aby zaimportować cokolwiek w tym pakiecie (np. mysite.urls).
mysite/__init__.py:                     Pusty plik, który mówi Pythonowi, że ten katalog powinien być uważany za pakiet Pythona. Jeśli
                                        jesteś początkujący w Pythonie, przeczytaj więcej o pakietach w oficjalnej dokumentacji Pythona.
mysite/settings.py:                     Ustawienia/konfiguracja dla tego projektu Django. Django settings powie ci wszystko o tym, jak 
                                        działają ustawienia.
mysite/urls.py:                         Deklaracje URL-i dla tego projektu Django; „spis treści” twojej strony opartej na Django. 
                                        Możesz przeczytać więcej o URL-ach w URL dispatcher.
mysite/asgi.py:                         Punkt wejściowy dla serwerów WWW kompatybilnych z ASGI do serwowania twojego projektu. Zobacz 
                                        Jak wdrażać z ASGI po więcej szczegółów.
mysite/wsgi.py:                         Punkt wejściowy dla serwerów WWW kompatybilnych z WSGI do serwowania twojego projektu. Zobacz 
                                        Jak wdrażać z WSGI dla większej ilości szczegółów.
'''
# modyfikacja /settings.py
'''
TIME_ZONE = 'Europe/Warsaw'                           # strefa czasowa
LANGUAGE_CODE = 'pl-pl'                               # język

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')        # dodajemy pod STATIC_URL # ścieżkę do plików statycznych (nie będziemy musielipodawać ścieżki bezwzględnej, tylko zaczynamy od naszej ścieżki BASE_DIR)
STATIC_ROOT = BASE_DIR / 'static/'                     # dla wersji django 4.1 

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']  # potrzebne do przepuszczania hostów do pracy z Django,  
                                                      # 127.0.0.1 - local host,  .pythonanywhere.com - chmura pythonowa

### sqlite3 ###
zmiana bazy danych ( my korzystamy z sqlite3)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
### mongoDB ###
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'Baza_danych',
        'HOST': '127.0.0.1',
        'PORT': 27017,

### sql ###
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'Baza_danych',
        'HOST': 'db.server.twoja-domena.pl',
        'PORT': '1433',
        'NAME': 'user',
        'PASSWORD': 'hasło',
        'OPTIONS':{
            'driver': 'Nazwa sterownika',
            'unicode_result': True,
        }
'''

# 3. Instalacja/obsługa git

'''
windows - można ściągnąc bezpośrednio ze strony lub zainstalować przez visual studio code
linux-  & sudo apt install git

git init  							                        -  inicjalizacja nowego (pustego) repezytorium		Zainicjowano puste repozytorium Gita w /home/micha/venv/.git/
git status 							                        -  taka jakby historia gita
git add --all  							                    -  dodanie plików do repezytorium
git config --global user.email "grabarzmichal@gmail.com"   	-  ustalenie adresu email dla konta na github
git config --global user.name "Michał Grabarz"			    -  nazwa użytkownika github
git commit -m "Pierwszy zrzut plików"  				        -  komentarz do zrzutu plików. Po poprawnym wykonaniu otrzymamy inf. jak niżej:

[master (zapis-korzeń) dc0ec99] Pierwszy zrzut plików
 17 files changed, 429 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 01 pliki projektu.py
 create mode 100644 02 tworzenie pierwszej aplikacji.py
 create mode 100644 blog/__init__.py
 create mode 100644 blog/admin.py
 create mode 100644 blog/apps.py
 create mode 100644 blog/migrations/0001_initial.py
 create mode 100644 blog/migrations/__init__.py
 create mode 100644 blog/models.py
 create mode 100644 blog/tests.py
 create mode 100644 blog/views.py
 create mode 100755 manage.py
 create mode 100644 mysite/__init__.py
 create mode 100644 mysite/asgi.py
 create mode 100644 mysite/settings.py
 create mode 100644 mysite/urls.py
 create mode 100644 mysite/wsgi.py
 
git remote add origin https://github.com/bioly1910/venv.git	-  trzy komendy aby dodać repezytorium dokonta github(Uwaga, zamiast hasła musisz wpisać token)
git branch -M main
git push -u origin main
'''

