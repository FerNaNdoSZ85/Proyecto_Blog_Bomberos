from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    id_cat = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=False, null=False)
    activado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta: #? Esto me muestra el plural de categoria --> buenas practicas
        verbose_name_plural = "Categorias"
    
    def __str__(self): #? esto me muestra el nombre y no la posicion de memoria
        return str(self.nombre)

class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=40, blank=False, null=False)
    resumen = models.CharField(max_length=70 , blank=False, null=False)
    texto = models.TextField(max_length=500, blank=False, null=False)
    imagen = models.ImageField(upload_to= 'post', null=True)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    publicado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def Meta():
        verbose_name_plural = 'Posteos'
    def __str__(self):
        return str(self.titulo)
