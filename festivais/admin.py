from django.contrib import admin
from .models import Festival
from .models import Localizacao
from .models import Banda


admin.site.register(Festival)
admin.site.register(Localizacao)
admin.site.register(Banda)

