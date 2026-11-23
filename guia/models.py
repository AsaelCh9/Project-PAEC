from django.db import models

class ConsultaComposta(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Tu nombre")
    pregunta = models.TextField(verbose_name="¿Cuál es tu duda sobre el compostaje?")
    respuesta = models.TextField(blank=True, null=True, verbose_name="Respuesta del experto")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

    def __str__(self):
        return f"{self.nombre} - {self.pregunta[:30]}..."