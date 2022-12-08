# 1. w katalogu djangoblog/blog/templates/blog tworzymy plik base.html
# 2. Kopiujemy całą zawartośc pliku post_list.html do pliku base.html
# 3. usuwamy całą zawartość kontenera <body>
# 4. tworzymy nowe drzewo kontenerów w <body>
# 5. umieszczamy znaczniki django w kodzie base.html {% bolck content %}{% endblock %}
     # plik wygląda tak:
'''
<!DOCTYPE html>
{% load static %}
<html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Blog dla programistów</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
        <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    </head>
<body>
<div class="page-header">   
    <h1><a href="/">Blog dla programistów</a></h1>
</div>
<div class="content container">
    <div class="row">
        <div class="col-md-8">
            {% bolck content %}                                 w to miejsce
            {% endblock %}                                      wstawimy nasz zmodyfikowany plik post_list
        </div>
    </div>
</div>
</body>
</html>
'''

# 6. Modyfikujemy plik post_list.html do takiej postaci:

'''

'''