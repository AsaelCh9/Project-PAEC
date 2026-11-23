from django.contrib import admin
from .models import ConsultaComposta

@admin.register(ConsultaComposta)
class ConsultaCompostaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pregunta', 'fecha_creacion', 'tiene_respuesta')
    search_fields = ('nombre', 'pregunta')

    def tiene_respuesta(self, obj):
        return bool(obj.respuesta)
    tiene_respuesta.boolean = True
    tiene_respuesta.short_description = "Respondida"