# 1. w pliku blog/urls.py dodajemy path (ścieżkę)
'''
path('post/<int:pk>/image/', views.image_fullscreen, name='image_fullscreen'),
'''
# 2. w pliku blog/vievs.py dodajemy widok:
    # ze względu na różnice w formatowaniu, tworzymy nowy plik bez podstawiania do pliku bazowego base.html
'''
def image_fullscreen(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/image_fullscreen.html', {'post': post})
'''
# 3. tworzymy plik html blog/templates/blog/image_fullscreen.html
'''
{% load static %}
<html lang="pl">
    <head>
        <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
            <link rel="stylesheet" href="{% static 'css/blog.css' %}">
            <script src="https://use.fontawesome.com/451851369b.js"></script>
            <link href="https://fonts.googleapis.com/css2?family=Inter&display=swap" rel="stylesheet">
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>   
    </head>
<body> 
 <div class="padding-fullscreenViev">
    <div class="navbar navbar-light" style="background-color: #061A40; border-radius: 10px" >
        <h1><a class="fullscreenViev" href="/">Blog dla programistów</a></h1><br/>
    </div>
    <div>
        <a href="{% url 'post_detail' pk=post.pk %}"><img src="{{ post.image.url }}" class="imagefsv" alt="Obrazek" width="100%">
    </div>
</div>
</body>
</html>
'''