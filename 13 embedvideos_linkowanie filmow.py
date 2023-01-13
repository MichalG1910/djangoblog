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
