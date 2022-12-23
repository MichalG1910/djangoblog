from django.contrib import admin
from .models import Post # . przed models oznacza, że odnosimy się do pliku models z bieżącego katalogu
from embed_video.admin import AdminVideoMixin

              # rejestrujemy nasz model Post

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Post, MyModelAdmin)

