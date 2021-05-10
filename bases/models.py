from django.db import models
from django.contrib.auth.models import User

class ClaseModelo (models.Model):
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateField(auto_now_add=True)
    fechaModificado = models.DateField(auto_now=True)  #Por cada accion se actualiza la fecha (insertar, actualizar)#
    usuarioCrea = models.ForeignKey(User,on_delete=models.CASCADE)
    usuarioModifica = models.IntegerField(blank=True,null=True)

    class Meta:
        abstract=True
