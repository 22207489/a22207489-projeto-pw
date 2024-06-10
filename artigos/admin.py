
from django.contrib import admin
from .models import Autor
from .models import Artigo
from .models import Comentario
from .models import Avaliacao


admin.site.register(Autor)
admin.site.register(Artigo)
admin.site.register(Comentario)
admin.site.register(Avaliacao)


