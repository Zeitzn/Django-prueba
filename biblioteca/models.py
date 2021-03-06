from django.db import models

# Create your models here.

class Editor(models.Model):
    nombre=models.CharField(max_length=30)
    domicilio=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=60)
    estado=models.CharField(max_length=30)
    pais=models.CharField(max_length=50)
    website=models.URLField()

    class Meta:
        verbose_name_plural="Editores"

class Autor(models.Model):
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=40)
    email=models.EmailField()
    class Meta:
        verbose_name_plural="Autores"

class Libro(models.Model):
    titulo=models.CharField(max_length=100)
    autores=models.ManyToManyField(Autor)
    editor=models.ForeignKey(Editor, null=True,blank=True, on_delete=models.CASCADE)
    fecha_publicacion=models.DateField()
    portada=models.ImageField(upload_to='portadas')
