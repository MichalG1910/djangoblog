'''css - kaskadowe arkusze stylów'''
# 18. wchodzimy na stroę getbootstrap.com
#     w pliku post_list.html w kontenerze <head> wklejamy połączenie do css bootstrap <!-- CSS only -->
# <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
'''
<!DOCTYPE html>
<html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Blog dla programistów</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    </head>
<body>
'''

# 19. tworzymy pliki statyczne, które przechowują arkusze stylów(czyli wszystkie definicje związane z wyglądem strony, obrazki i tp)
#     tworzymy w katalogogu blog nowy katalog static (tak się utarło, że tworzymy go w tym miejscu i tak nazywamy), a w nim katalog css (dla porządku) /djangoblog/blog/static/css
#     w /djangoblog/blog/static/css tworzymy plik blog.css
'''
h1 a, h2 a{                     ten zapis tworzy połączenie między naszymi znacznikami (nagłowkami) h1,h2 w pliku post_list z ancor(kotwicami) a
    color: #DE781F;             definiujemy dla nich kolor (kolory możesz dopasować dzięki stronom ww color-picker. Przykładowa: https://www.webfx.com/web-design/color-picker/
}                               #DE781F - wersja koloru hex
'''
#    h1 a  -  to tzw selektor css - zastosujemy nasze style do każdego elementu, który będzie zawierał tag "a" i na dodatek będzie znajdowal się w elemencie h1
#    istnieje kilka metod rozpoznawania elementów:
#    - po tagach (jak wyżej)
#    - atrybutach klas
#    - Id

# 20. w pliku post_list wstawiamy znaczniki django: {% load static %}
#     oraz dodajemy w <head> za naszym linkiem bootstrapowym link : <link rel="stylesheet" href="{% static 'css/blog.css' %}">
#     (jest w nim wskazana lokalizacja naszego pliku blog.css)
'''
<!DOCTYPE html>
{% load static %}                                   odpowiada on za ładowanie plików statycznych tj: /djangoblog/blog/static/css/blog.css
<html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Blog dla programistów</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
        <link rel="stylesheet" href="{% static 'css/blog.css' %}">              
    </head>
'''
# może dojść do sytuacji, że ładoowanie naszego css nie zadziała, wtedy:
'''

{% load static %}                                   odpowiada on za ładowanie plików statycznych tj: /djangoblog/blog/static/css/blog.css
<html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Blog dla programistów</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
        <link rel="stylesheet" href="{% static 'css/blog.css' %}">              
    </head>
'''
# 21. modyfikujemy w naszym pliku post_list znacznik h1 aby był on podświetlony na pomarańczowo
#     <h1>Witam na stronie bloga!</h1> ---> <h1><a href="post_list.html">Witam na stronie bloga!</a></h1>

# 22. w pliku /djangoblog/blog/static/css/blog.css dokonujemy zmiany stylów kolejnych elementow naszego pliku(strony post_list)
# 
'''
h1 a, h2 a{
    color: #DE781F;
}

body {                                          wszytko co znjduje się w kontenerze <body> będzie miało padding 15 (odsunięcie od lewej strony o 15 pikseli)
    padding-left:15px;
    font-family: 'Lato', sans-serif;            zmieniamy czcionkę (użyłem strony: https://fonts.google.com/). Można też skopiować link i wkleić go w pliku post_list w sekcji <head> : <link rel="preconnect"href="https://fonts.googleapis.com">
                                                                                                                                                                                        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                                                                                                                                                                                            <link href="https://fonts.googleapis.com/css2?family=Lato&display=swap" rel="stylesheet">                                                                                                                                                                                                
}
''' 
# 23. tworzymy i wykorzystujemy nazwy KLAS w naszych kontenerach

'''
<div class="page-header">                                                     utworzono nazwę klasy
        <h1><a href="post_list.html">Witam na stronie bloga!</a></h1>    
        <h2>Blog o programowaniu</h2>    
        <h3>Autor: Michał</h3>    
        <h4>wszelkie prawa zastrzeżone</h4> 
    </div>
    {% comment "Komentarz- w cudzysłowiu tytuł komentarza"%}
    Wszystko, co się znajdzie między początkiem i końcem
    komentarza, nie bedzie wykonywane przez django
    {% endcomment %}
    
    {% for post in posts %} 
    <div class="post">                                                          utworzono nazwę klasy
        <p>opublikowany: {{ post.publish_date }}</p>
        <h2><a href="">{{ post.title }}</a></h2> 
        <em>{{ post.text|linebreaksbr }}</em>
    </div>
    {% endfor %}
    <div class="stopka">                                                        utworzono nazwę klasy
        
    </div>
'''

# dodajemy w naszym pliku body.css (odnosimy się do naszych klas)

'''
.page-header{
    background-color: #C25100;                  kolor tła
    margin-top: 0;                              margines
    padding: 20px 20px 20px 40px                lewy, prawy, gora, dół
}
'''
# możemy jednocześnie odnosić się do kilku elementów w klasie:
'''
.page-header h1, .page-header h1 a, .page-header h1 a:visited, .page-header h1 a:active {
    color: #ffffff;
    font-size: 36 pt;
    text-decoration: none;
}
'''
# modyfikujemy hierarchię pliku post_list.html, aby stworzyć kontener w  innym kontenerze (z nazwą klasy) inadajemy mu nazwę klasy:
'''
<div class="post">
        <div class="data">
            <p>opublikowany: {{ post.publish_date }}</p>
        </div>
        <h2><a href="">{{ post.title }}</a></h2> 
        <em>{{ post.text|linebreaksbr }}</em>
    </div>
-------------------------------------------------------------------
    po tej operacji dodajemy styl tej klasy w blog.css
-------------------------------------------------------------------
.data {
    color: #828282;
}
'''
# 24. dalsza część modyfikacji:
'''
<div class="content container">
    <div class="row">
    {% for post in posts %}
    <div class="col-md-8"> 
        <div class="post">
            <div class="data">
                <p>opublikowany: {{ post.publish_date }}</p>
            </div>
            <h2><a href="">{{ post.title }}</a></h2> 
            <em>{{ post.text|linebreaksbr }}</em>
        </div>
        {% endfor %}
    </div>
</div> 
</div>
'''
   # plik blog.css

'''
}
.content {
    margin-left: 40px;
    
}
h1, h2, h3, h4 {
    font-family: 'Lobster', cursive;
}

.save {
    float: right;
}

.post-form textarea, .post-form input {
    width: 100%;
}

.top-menu, .top-menu:hover, .top-menu:visited{
    color: #ffffff;
    float: right;
    font-size: 26pt;
    margin-right: 20px;
}

.post {
    margin-bottom: 70px;
}

.post h2 a, .post h1 a:visited {
    color: #000000
}
'''

