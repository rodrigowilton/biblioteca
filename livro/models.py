from django.db import models
from datetime import date
from usuarios.models import Usuario
import datetime

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nome


class Livros(models.Model):
    nome = models.CharField(max_length=60)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30, blank=True)
    # para cadastrar a data automatica do dia (default=date.today)
    data_cadastro = models.DateField(default=date.today)
    emprestado = models.BooleanField(default=False)
    # para deixar cadastrar em branco o campo (blank=True, null=True)

    categoria = models.ForeignKey(Categoria,on_delete= models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario,on_delete=models.DO_NOTHING)


    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome


class Emprestimos(models.Model):
    choices = (
        ('P', 'Péssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Ótimo')

    )
    nome_emprestado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank=True, null=True)
    nome_emprestado_anonimo = models.CharField(max_length=30, blank=True, null=True)
    data_emprestimo = models.DateTimeField(default=datetime.datetime.now())
    data_devolucao = models.DateTimeField(blank=True, null=True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)
    avaliacao = models.CharField(max_length=1, choices=choices, blank=True, null=True)


    def __str__(self):
        return f"{self.nome_emprestado} | {self.livro}"



