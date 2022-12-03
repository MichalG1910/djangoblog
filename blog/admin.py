from django.contrib import admin
from .models import Post # . przed models oznacza, że odnosimy się do pliku models z bieżącego katalogu

admin.site.register(Post)               # rejestrujemy nasz model Post

