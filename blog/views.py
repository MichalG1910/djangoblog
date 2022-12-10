from django.shortcuts import render, get_object_or_404  # get_object_or_404 - daj obiekt (pobierz) albo wyświetl 404 (błąd page not found)  
from .models import Post # . przed models oznacza, że odnosimy się do pliku models z bieżącego katalogu
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date') # tworzymy zmienną posts, która będzie zawierała posty posegregowane według daty publikacji
    return render(request, 'blog/post_list.html', {'posts': posts})
# funkcja post_list pobiera(request) i zwraca(return) wartość uzyskaną dzięki wywołaniu innej funkcji (render - funkcja renderuje(składa w całość szablon HTML))

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})