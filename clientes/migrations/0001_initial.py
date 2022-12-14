# Generated by Django 4.1.2 on 2022-10-11 22:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('cpf', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_ativo', models.CharField(max_length=10)),
                ('quantidade_ativos', models.IntegerField(default=0)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('operacao', models.CharField(choices=[('C', 'Compra'), ('V', 'Venda')], max_length=1)),
                ('data_operacao', models.DateField(default=datetime.date.today(), null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
        ),
    ]
