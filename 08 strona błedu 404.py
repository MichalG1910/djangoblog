# 1. modyfikujemy plik mysite/settings.py

'''
DEBUG = False                       było Debug = True - jest to wersja produkcyjna naszej strony
TEMPLATE_DEBUG = DEBUG
'''

# 2. w pliku mysite/urls.py dodajemy

'''
handler404 = 'blog.views.error_404_view'            uchwyt do widoku naszej strony błedu 404
'''

# 3. w pliku blog/views.py dopisujemy funkcję obsługi widoku błędu 404

'''
def error_404_view(request, exception):
    data = {"name": 'Blog dla programistów'}
    return render(request, 'blog/404.html', data)
'''

# 4. w katalogu blog/templates/blog tworzymy plik 404.html

'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Strona z błędem 404</title>
</head>
<body>
    <em>TUTAJ INFORMACJE O błędach :)</em>
</body>
</html>
'''