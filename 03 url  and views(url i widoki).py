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

