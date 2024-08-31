from django.contrib import admin
from .models import Socio, Caracter, Sexo, EstadoCivil, Parentesco

admin.site.register(Socio)
admin.site.register(Caracter)
admin.site.register(Sexo)
admin.site.register(EstadoCivil)
admin.site.register(Parentesco)