from django.contrib import admin
from .models import Banda
from .models import Musica
from .models import Album

admin.site.register(Banda)
admin.site.register(Musica)
admin.site.register(Album)
