from django.shortcuts import render
from .models import Post # . przed models oznacza, że odnosimy się do pliku models z bieżącego katalogu
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date') # tworzymy zmienną posts, która będzie zawierała posty posegregowane według daty publikacji
    return render(request, 'blog/post_list.html', {'posts': posts})
# funkcja post_list pobiera(request) i zwraca(return) wartość uzyskaną dzięki wywołaniu innej funkcji (render - funkcja renderuje(składa w całość szablon HTML))