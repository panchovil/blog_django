# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Entrada(models.Model):
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Todas las Entradas"
        ordering = ['-fecha']
    titulo = models.CharField(u'Título', max_length = 100)
    fecha = models.DateTimeField(u'Fecha del Post',auto_now_add=True)
    resumen= models.CharField(u'Resumen',max_length=512)
    contenido = models.TextField(u'Contenido')
    def __str__(self):
        return self.titulo

class Mensajes(models.Model):
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
    nombre = models.CharField('Nombre:', max_length = 100)
    contenido = models.TextField('Mensaje:')
    able = models.BooleanField('Habilitado:', default = True)
    pub_en = models.ForeignKey(Entrada)
    def __str__(self):
        return self.nombre