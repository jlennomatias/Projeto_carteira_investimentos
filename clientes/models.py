from django.db import models
from datetime import date

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cpf = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.nome

class Carteira(models.Model):
    OPERACAO = (
        ('C', 'Compra'),
        ('V', 'Venda')
    )

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    codigo_ativo = models.CharField(max_length=10)
    quantidade_ativos = models.IntegerField(null=False, blank=False, default=0)
    preco = models.DecimalField(max_digits=10, null=False, blank=False, decimal_places=2)
    operacao = models.CharField(max_length=1, choices=OPERACAO, null=False, blank=False)
    data_operacao = models.DateField(null=True, blank=False, default=date.today)

    def __str__(self):
        return self.codigo_ativo
        