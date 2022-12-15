# 1. modyfikujemy plik blog/forms.py
#       zmodyfikowano klasę ImgForm - nzmieniono nazwę na PostForm

'''
class PostForm(forms.ModelForm):                    formularz jest jednocześnie formularzem modelu ModelForm (dzięki temu django wyręczy nas w pewnych czynnościach)
    class Meta:
        model = Post                                informacja, jaki model powinień być wykorzystany do stworzenia formularza
        fields = ['title', 'text', 'image']         pola, jakie powinny pojawić się w formularzu
'''

# 2. modyfikujemy plik blog/templates/blog/base.html
# dodajemy w kontenerze page-header
'''
<div class="page-header">  
    <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>      dodano. kotwica kieruje nas do url post_new; użyjemy grafiki wbudowanej w bootstrap - class="glyphicon glyphicon-plus"
    <h1><a href="/">Blog dla programistów</a></h1>
'''

# 3. dodajemy nowy url w pliku blog/urls.py

'''
path('post/new/', views.post_new, name='post_new'),
'''

# 4. dodajemy funkcję post_new w pliku blog/views.py
#       z uwagi na zmienienie nazwy klasy ImgForm w pliku forms.py(patrz pkt. 1), musimy w pliku views.py rownierz zamienić
#       wszystkie odnośniki korzystające z tej klasy na PostForm

'''
def post_new(request):
    form = PostForm
    return render(request, 'blog/post_edit.html', {'form': form})
'''

# 4. w katalogu blog/templates/blog tworzymy plik post_edit.html
#       uwaga! w tutorialu nie było enctype="multipart/form-data" w linii 42 (form method). Nie dało się dodawać z naszego formularza zdjęć, tylko sam tekst. 
'''
{% extends 'blog/base.html' %}                                                              podłączenie naszego szablonu base.html

{% block content %}
<h2>Nowy post</h2>
<form method="post" enctype="multipart/form-data" class="post-form">{% csrf_token %}        uruchamiamy naszform z metodą post; class="post-form" - klasa wyglądu z bootstrap; {% csrf_token %} - token dla bezpieczeństwa formularza
{{ form.as_p }}                                                                             uruchomienie formularza
    <button type="submit" class="save btn btn-default">Zapisz</button>                      button(przycisk) o typie submit; wygląd z klasy bootstrap 
</form>
{%  endblock %}
'''
# 4. modyfikujemy funkcję post_new w pliku blog/views.py
#       oraz dodajemy import funkcji redirect
#       uwaga, w tutorialu nie było request.FILES w linii 56(form = form = PostForm(request.POST, request.FILES). Nie dało się dodawać z naszego formularza zdjęć, tylko sam tekst.
'''
from django.shortcuts import render, get_object_or_404, redirect        dodaliśmy redirect

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()   
    return render(request, 'blog/post_edit.html', {'form': form})
'''
