# 1. instalujemy wtyczkę embedvideos (pip install django-embed-video)
    # https://django-embed-video.readthedocs.io/en/latest/

# 2. dokonujemy zmian w pliku blog/mysite/settings.py
    # do INSTALLED_APS dodajemy wpis:
'''
INSTALLED_APPS = [
    'embed_video'
]
'''
    # w TEMPLATES dodajemy wpis(uwaga, może on już być obecny)
'''
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',                   ten wpis dodajemy, jak go nie ma
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]  
'''

# 3. dodajemy do zmiennej fields w pliku blog/forms.py wpis:
'''
class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'url']          dodano pole url - w nim będziemy wklejać link do naszego video
'''

# 4. modyfikujemy plik blog.models.py
    # robimy import biblioteki 
'''
from embed_video.fields import EmbedVideoField
'''

    # w class Post(models.Model) dodajemy wpis:
'''
url = EmbedVideoField(null=True, blank=True)                pole do wpisania naszeo adresu url do video
'''

# 5. w pliku blog/admin.py dodajemy wpisy:
    # importujemy biblioteki
'''
from embed_video.admin import AdminVideoMixin
'''
    # tworzymy class, która umożliwi dodanie video z poziomu administratora (wyświetli go też w panelu administratora)
'''
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
'''
# 6. Modyfikujemy plik blog/templates/blog/post_list.html (na stronie głównej odpowiada za wyświetleni listy dodanych postów)
'''
{% extends 'blog/base.html' %}
    {% load embed_video_tags %}                     zapis powoduje, że wszystkie tagi z video będą czytane (jest konieczny)
    {% block content %}
    {% for post in posts %}
        <div class="post">
            {% if post.image %}
            <a href="{% url 'image_fullscreen' pk=post.pk %}"><img src="{{ post.image.url }}" class="img" alt="Obrazek" width="300px"></a><br/>
            {% elif post.url %}
            <div class="vid">       
                {% video post.url '300x200' %}      nasze video (korzysta z modelu w pliku blog/models class Post() korzystając ze zmiennej url, dlatego zapis: {% video post.url '300x200' %})
            </div>    
            {% endif %}           
            <div class="data">
            <p>opublikowany: {{ post.publish_date }}</p>
            </div><h2><b><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></b></h2><br/>    
            <em>{{ post.text|linebreaksbr }}</em></div><br/>  
    {% endfor %}
    {% endblock %}
'''
    # wykorzystano tu instrukcje warunkową if {% if post.image %} oraz elif {% elif post.url %} - w naszej liście postów wstawi miniaturę obrazu, a jak
    # go nię będzie to miniaturę filmu. Jeśli nie będzie w poście ani image ani video, post będzie zawierał sam tekst

# 7. Modyfikujemy plik blog/templates/blog/post_detail.html dodając linie odpowiedzialne za video

'''
{% extends 'blog/base.html' %}
{% load embed_video_tags %}                 dodano linię
{% block content %}
<div class="post">
    {% if post.published_date %}
    <div class="date">
        {{ post.publish_date }}
    </div>
    {% endif %}
    {% if user.is_authenticated %}
    <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    {% endif %}
    <h2>{{ post.title }}</h2>
    {% if post.image %}
    <a href="{% url 'image_fullscreen' pk=post.pk %}"><img src="{{ post.image.url }}" class="img" alt="Obrazek" width="100%"></a>
    {% endif %}            
    {% video post.url '850x700' %}          dodano linię
    <p>{{ post.text|linebreaksbr }}</p>
</div>
{% endblock %}
'''