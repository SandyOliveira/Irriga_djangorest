from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Setor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Sensores(models.Model):
    nome = models.CharField(max_length=50)
    setor = models.ForeignKey("Setor",  on_delete=models.CASCADE)
    estado = models.BooleanField(default=0)
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Registro(models.Model):
    acao = models.CharField(max_length=50)
    data_hora = models.CharField(max_length=50)
    valor= models.CharField(max_length=50)
    usuario = models.ForeignKey("Usuario",  on_delete=models.CASCADE)
    sensores = models.ForeignKey("Sensores",  on_delete=models.CASCADE)

    def __str__(self):
        return self.data_hora


class Agendar(models.Model):
    hora_inicio = models.CharField(max_length=50)
    hora_fim = models.CharField(max_length=50)
    intervalo = models.CharField(max_length=50)

    def __str__(self):
        return self.data_hora
