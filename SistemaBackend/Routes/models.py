from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class Usuario(AbstractUser):
    nombre_user = models.CharField(max_length=50,null=False,blank=False,unique=True)
    password = models.CharField(max_length=128)
    def save(self, *args, **kwargs):
        # Encriptar la contraseña si es user nuevo
        if not self.pk:  
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username
