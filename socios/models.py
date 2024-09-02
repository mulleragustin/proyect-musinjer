from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils import timezone

class Caracter(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Sexo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class EstadoCivil(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Socio(models.Model):
    ESTADO_CHOICES = [
        ('A', 'Activo'),
        ('S', 'Suspendido'),
        ('B', 'Baja'),
    ]

    socio_id = models.IntegerField(primary_key=True)
    dni = models.IntegerField(unique=True, validators=[MaxValueValidator(999999999), MinValueValidator(1000000)])
    caracter = models.ForeignKey(Caracter, on_delete=models.SET_NULL, null=True)
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    sexo = models.ForeignKey(Sexo, on_delete=models.SET_NULL, null=True)
    fec_nac = models.DateField(null=True, blank=True)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.SET_NULL, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    localidad = models.CharField(max_length=100)
    celular = models.IntegerField(blank=True, null=True)
    telefono = models.IntegerField( blank=True, null=True)
    email = models.EmailField(unique=False)
    dependencia = models.CharField(max_length=100, blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    funcion = models.CharField(max_length=100, blank=True, null=True)
    domicilio_laboral = models.CharField(max_length=255, blank=True, null=True)
    telefono_laboral = models.IntegerField( blank=True, null=True)
    estado= models.CharField(choices=ESTADO_CHOICES, default='A', blank=False,max_length=1)
    created_by = models.ForeignKey(User, related_name='socio_created_by', on_delete=models.SET_NULL, null=True, blank=True)
    modified_by = models.ForeignKey(User, related_name='socio_modified_by', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.apellido} {self.nombre}"

    def save(self, *args, **kwargs):
        if not self.socio_id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super(Socio, self).save(*args, **kwargs)

class Parentesco(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
   

    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    dni_familiar = models.IntegerField()
    parentesco = models.ForeignKey(Parentesco, on_delete=models.SET_NULL, null=True)
    apellido_familiar = models.CharField(max_length=100)
    nombre_familiar = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.get_parentesco_display()} de {self.socio}"

