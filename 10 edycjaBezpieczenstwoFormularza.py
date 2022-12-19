# 1. modyfikujemy plik blog.forms.py
#       w class PostForm dodajemy

'''
title = forms.CharField(help_text='maksymalnie 200 znaków')
'''

# 2. dodajemy wpis <a class... w pliku blog/templates/blog/post_detail.py

'''
{% endif %}
<a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
<h2>{{ post.title }}</h2>
'''

# 3. dodajemy nową ścieżkę path w pliku blog/urls.py

'''
path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
'''

# 4. dodajemy funkcję widoku post_edit w pliku blog/views.py

'''
def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)   
    return render(request, 'blog/post_edit.html', {'form': form})
'''

# 5. wpisujemy instrukcję warunową if w pliku blog/templates/blog/base.html
#       instrukcja ta w←świetli nasz "+" odpowiedzialny za dodanie posta tylko wtedy, kiedy użytkownik będzie zalogowany

'''
{% if user.is_authenticated %}  
<a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
{% endif %}
'''
#       to samo robimy z blog/templates/blog/post_detail.html
#       (wyświetlany ołówek do edycji posta)
'''
{% if user.is_authenticated %}
<a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
{% endif %}
'''