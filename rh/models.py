from django.db import models

# Create your models here.
class Produtos(models.Model):
    imagem = models.ImageField(null=True,blank=True)
    produto = models.CharField(max_length=100,null=True,blank=True)
    categoria = models.CharField(max_length=100,null=True,blank=True)
    descricao = models.TextField(max_length=100,null=True,blank=True)
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    em_estoque = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos" # Define o nome plural correto
    def __str__(self):
        return self.produto

class Funcionarios(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    data_contratacao = models.DateField()
    status = models.BooleanField(default=True)

    #corrige o problema de duplo 's' no nome do modelo no admin
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários" # Define o nome plural correto
    def __str__(self):
        return self.nome
        
    # contato/models.py
from django.db import models
from django.utils import timezone

class MensagemContato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(default=timezone.now)
    lido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.assunto} - {self.nome} ({self.email})"

    class Meta:
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"
        ordering = ['-data_envio']

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    idade = models.IntegerField(default=0, blank=True, null=True)
    email = models.EmailField()
    contato = models.IntegerField(default=0, blank=True, null=True)

    