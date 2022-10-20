from email.policy import default
from genericpath import exists
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Cliente, Carteira
import re
from datetime import date
from django.contrib import messages
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.urls import reverse


def clientes(request):
    if request.method == "GET":
        clientes_list = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes': clientes_list})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        codigo_ativos = request.POST.getlist('codigo_ativo')
        quantidade_ativos = request.POST.getlist('quantidade_ativos')
        precos = request.POST.getlist('preco')
        operacoes = request.POST.getlist('operacao')
        data_operacoes = request.POST.getlist('data_operacao')

        cliente = Cliente.objects.filter(cpf=cpf)

        if cliente.exists():
            messages.error(request,'O usuario já existe')
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'carteira': zip(codigo_ativos, quantidade_ativos, precos, operacoes, data_operacoes)})
        
        if not re.fullmatch(re.compile(r'^\d{11}$'), cpf):
            messages.error(request,'cpf precisa ter 11 caracteres')
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'carteira': zip(codigo_ativos, quantidade_ativos, precos, operacoes, data_operacoes)})

        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            messages.error(request,'email ja existe')
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'carteira': zip(codigo_ativos, quantidade_ativos, precos, operacoes, data_operacoes)})

        cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )

        cliente.save()
        
        for ativo, quantidade, valor, operacao, data_operacao in zip(codigo_ativos, quantidade_ativos, precos, operacoes, data_operacoes):
            if not data_operacao:
                data_operacao = date.today()

            carteira = Carteira(codigo_ativo=ativo, quantidade_ativos=quantidade, preco=valor, operacao=operacao, data_operacao=data_operacao, cliente=cliente)
            carteira.save()
        
        return HttpResponse('teste')


def att_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    cliente = Cliente.objects.filter(id=id_cliente)
    ativos = Carteira.objects.filter(cliente=cliente[0])
    cliente_json = json.loads(serializers.serialize('json', cliente))[0]['fields']
    cliente_id = json.loads(serializers.serialize('json', cliente))[0]['pk']
    ativos_json = json.loads(serializers.serialize('json', ativos))
    ativos_json = [{'fields': ativo['fields'], 'id': ativo['pk'] } for ativo in ativos_json]

    data = {'cliente': cliente_json, 'ativos': ativos_json, 'cliente_id': cliente_id}
    return JsonResponse(data)

@csrf_exempt
def update_ativo(request, id):
    codigo_ativo = request.POST.get('ativo')
    quantidade_ativos = request.POST.get('quantidade')
    preco = request.POST.get('preco')
    data_operacao = request.POST.get('data')

    ativo = Carteira.objects.get(id=id)
    print(ativo)
    return HttpResponse(codigo_ativo)

def excluir_ativo(request):
    try:
        ativo = Carteira.objects.get(id=id)
        ativo.delete()
        return redirect(reverse('clientes')+f'?aba=att_cliente&id_cliente={id}')
    except:
        return redirect(reverse('clientes')+f'?aba=att_cliente&id_cliente={id}')

def update_cliente(request, id):
    pass



