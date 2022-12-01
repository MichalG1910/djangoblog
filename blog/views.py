from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
# funkcja post_list pobiera(request) i zwraca(return) wartość uzyskaną dzięki wywołaniu innej funkcji (render - funkcja renderuje(składa w całość szablon HTML))