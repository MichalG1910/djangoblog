# 1. modyfikujemy plik post_list.html

'''
<h2><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h2>          w naszym href wprowadzamy zapytanie django
# url 'post_detail' - django będzie oczekiwał takiego bloky w pliku blog/urls.py  ;  
# pk=post.pk (primary key - klucz podstawowy) django będzie dodawał liczbę+1 do każdego rekordu post (będzie numerował nasze posty) 
'''

# 2. w pliku blog/urls.py dodajemy blok:

'''
path('post/<int:pk>/', views.post_detail, name='post_detail'),
# <int:pk> - django będzie spodziewało liczby całkowiteji przekaże jej wartośc do widoku jako zmienną pk
'''

# 3.  w pliku blog/views.py dodajemy:

'''
from django.shortcuts import render, get_object_or_404  # dodajemy get_object_or_404 - daj obiekt (pobierz) albo wyświetl 404 (błąd page not found) 

def post_detail(request, pk):                                               stworzyliśmy widok post_detail (używając zmiennej pk), jednak odnośi się on do jeszcze nieistniejącego szablonu post_detail.html
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
'''

# 4.  w katalogu blog/templates/blog tworzymy nowy szablon widoku post_detail.html

'''
{% extends 'blog/base.html' %}                  podłączenie szblonu base.html

{% block content %}
<div class="post">
    {% if post.published_date %}                pętla if wyrzucająca tylko obublikowane posty
    <div class="date">
        {{ post.publish_date }}
    </div>
    {% endif %}
    <h2>{{ post.title }}</h2>
    <p>{{ post.text|linebreaksbr }}</p>
</div>
{% endblock %}
'''