# 1. w pliku settings.py dodajemy

'''
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles/'
STATICFILES_DIR = BASE_DIR / 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'                        media - będzie to katalog, w którym umieścimy wszystkie media(video, obrazy, dzwięki)
'''

# 2. dokonujemy zmian w pliku mysite/urls.py

'''
from django.conf import settings
from django.conf.urls.static import static              dodane importy bibliotek
from blog.views import Image, ImageDisplay

# w urlpatterns dodajemy:

path('image/', Image.as_view(), name='image'),
path('image/<int:pk>/', ImageDisplay.as_view(), name='image_display'),

# tworzymy instrukcję warunkową sprawdzającą, czy jest w naszej aplikacji folder o nazwie MEDIA

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)              jeśli go nie będzie, to zostanie utworzony statycznie
'''

# 3. w pliku blog/views.py dokonujemy zmian:

'''
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy                        importujemy nowe biblioteki
from blog.forms import ImgForm
from django.views.generic import DetailView
from django.views.generic import TemplateView

# tworzymy klasy Image, ImageDisplay

class Image(TemplateView):
    form = ImgForm
    template_name = 'blog/image.html'

    def post(self, request, *args, **kwargs):
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('image_display', kwargs={'pk':obj.id}))
        
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ImageDisplay(DetailView):
    model = Post
    template_name = 'blog/image_display.html'
    context_object_name = 'image'
'''

# 4. tworzymy plik blog/forms.py

'''
from django import forms
from .models import Post


class ImgForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image']
'''

# 5. modyfikujemy plik blog/models.py

'''
dodajemy w class Post(models.Model):     
image = models.ImageField(null=True, blank=True, upload_to='images/')       # dodane zdjęcie (null=True - może to być 0, blank=True - może być puste, upload_to - gdzie ma być obraz zapisany)
'''

# 6. w katalogu blog/templates/blog tworzymy pliki:
#           image.html
'''
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">UPLOAD</button>
</form>
'''
#           image_display.html
'''
{% load static %}

<img src="{{ post.image.url }}" alt="Obrazek" width="250">
'''

# 7. modyfikujemy plik blog/templates/blog/post_list.html
#       nasza miniaturka obrazka zostanie wyświetlona pod postem
'''
<h2><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h2> 
    <img src="{{ post.image.url }}" alt="Obrazek" width="100px">                        dodano
<em>{{ post.text|linebreaksbr }}</em>
'''
# 7a. zmiana powyżej działała niepoprawnie. Jeśli choćby 1 post nie miał obrazka, wyrzucało błąd servera 500
#       Zmodyfikowałem dodając instrukcję warunkową:

'''
{% if post.image %}
    <img src="{{ post.image.url }}" alt="Obrazek" width="100px">
{% endif %}
'''

# 8. modyfikujemy plik blog/templates/blog/post_detail.html
#       Działało niepoprawnie, aby naprawić patrz punkt wyżej (7a)

'''
<h2>{{ post.title }}</h2>
<img src="{{ post.image.url }}" alt="Obrazek" width="250px">
<p>{{ post.text|linebreaksbr }}</p>
'''

# 9. w terminalu wpisujemy: python manage.py makemigrations