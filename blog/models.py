from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField

# klasa dla naszych postów
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # autor
    title = models.CharField(max_length=200)                          # tytuł, Charfield - pole daje możliwośc wpisania 200 znaków
    text = models.TextField()                                         # pole tekstu
    created_date = models.DateTimeField(default=timezone.now)         # pole z wczytaną aktualną datą i godziną 
    publish_date = models.DateTimeField(blank=True, null=True)        # data publikacji (może byc pusta, wtedy np. artykuł będzie czekał na publikację)
    image = models.ImageField(null=True, blank=True, upload_to='images/') # dodane zdjęcie (null=True - może to być 0, blank=True - może być puste, upload_to - gdzie ma być obraz zapisany)
    url = EmbedVideoField(null=True, blank=True)                      # pole do wpisania naszeo adresu url do video
    def publish(self):                                                # funkcja do publikacji artykułu
        self.publish_date = timezone.now()                            # zrobi to tylko wtedy gdy self.publish_date = timezone.now()
        self.save()                                                   # zapisanie artykulu

    def __str__(self):                                                # zwraca wlaściwość title zamieni na string i przekaże do klasy, która zapisze ją do bazy
        return self.title 