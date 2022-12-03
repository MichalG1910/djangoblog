# 11. /djangoblog  -  modyfikujemy plik urls.py

from django.contrib import admin
from django.urls import path, include # dodajemy include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'^admin/(/d+)$', admin.site.urls) # tzw regex (jest to zapis url z wyrażeniami regularnymi(możemy dzięki niemu np. rozróżniać posty przez dodanie cyfry do każdego z nich)). Jest to metoda przestarzała, rzadko już spotykana
    path('',include('blog.urls')) # dodajemy #''- pusty zapis powoduje, że gdy wpiszemy adres url(np. naszej strony 127.0.0.1:8000), to include podłączy do niego plik blog.urls
]
# 12. /djangoblog/blog tworzymy plik urls.py

from django.urls import path
from . import views # wszystkie widoki (które utworzymy) z aplikacji blog zostaną zaimportowane

urlpatterns = [
    path('', views.post_list, name='post_list'), # przyporządkowanie widoku post_list do strony głównej
    # views.post_list zostanie dopasowany do pustego ciągu znaków '', każdy kto wejdzie na 127.0.0.1 trafi na ten widok, name=post_list to nazwa url, która będzie używana do zidentyfikowania widoku
]

# 13. /djangoblog/blog  modyfikujemy plik views.py

from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
# funkcja post_list pobiera(request) i zwraca(return) wartość uzyskaną dzięki wywołaniu innej funkcji (render - funkcja renderuje(składa w całość szablon HTML))

# 14. w katalogu blog tworzymy katalog templates, a w nim kolejny katalog blog --> blog/templates/blog
# 15. blog/templates/blog tworzymy plik post_list.html 
# wywołanie "!" - tworzy szablon html w pliku: (uwaga, poniżej używamy języka html)
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">                                                      # kodowanie strony
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>                                                     # tytuł strony
</head>
<body>                                                                          # sekcja body - to tu umieścimy elementy naszej strony widoczne na ekranie
    
</body>
</html>
'''

# zmieniamy nasz szablon

'''
<!DOCTYPE html>
<html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Blog dla programistów</title>
    </head>
<body>
    <div>                                                       # znacznik <div> - kontener(pusty nic w naszym widoku nie zmienia). Po dodaniu znaczników CSS (znaczniki arkuszów stylów) możemy na przykład ustawić kolor tekstu w takim kontenerze
        <h1>Witam na stronie bloga!</h1>                        # znacznik <h1> header(tytuł) (h1 do h4 - od największego do najmniejszego)
        <h2>Witam na stronie bloga!</h2>    
        <h3>Witam na stronie bloga!</h3>    
        <h4>Witam na stronie bloga!</h4>
    </div>
    <div>
        <p>To jest akapit</p>                                   # znacznik <p>  paragraf - możesz później sformatować tekst w nim zawarty (np. czcionkę)
        <em>To jest wyróżniony tekst</em><br>                   # znacznik <em> wyróżnik - domyślnie to italic(pochylenie tekstu). Możesz ten znacznik stosować wewnątrz tekstu  <br> - enter(przejście do następnego wiersza)
        <strong>Tu jest pogrubiony tekst</strong><br>           # znacznik <strong>      - pogrubiony tekst
        <a href="https://strefakursów.pl">strefakursów.pl</a>   # wstawianie linku
    </div>
    <div>
        <ul>
            <li>Element listy</li>                              # elementy listy <ul> nadrzędny
            <li>Element listy</li>                                               <li> podrzędny
            <li>Element listy</li>
        </ul>
    </div>
</body>
</html>
'''

# 16. wprowadzamy dane dynamiczne do naszych widoków
#     /djangoblog/blog  modyfikujemy plik views.py

from django.shortcuts import render
from .models import Post # . przed models oznacza, że odnosimy się do pliku models z bieżącego katalogu
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date') # tworzymy zmienną posts, która będzie zawierała posty posegregowane według daty publikacji
    return render(request, 'blog/post_list.html', {'posts': posts}) # uzupełniliśmy {}

