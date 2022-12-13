"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import Image, ImageDisplay

urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'^admin/(/d+)$', admin.site.urls) # tzw regex (jest to zapis url z wyrażeniami regularnymi(możemy dzięki niemu np. rozróżniać posty przez dodanie cyfry do każdego z nich)). Jest to metoda przestarzała, rzadko już spotykana
    path('',include('blog.urls')), # ''- pusty zapis powoduje, że gdy wpiszemy adres url(np. naszej strony 127.0.0.1:8000), to include podłączy do niego plik blog.urls
    path('image/', Image.as_view(), name='image'),
    path('image/<int:pk>/', ImageDisplay.as_view(), name='image_display'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
