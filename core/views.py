from django.shortcuts import render, HttpResponse

# Create your views here.

def soma(request, n1, n2):
    soma = n1 + n2
    return HttpResponse(f'<h1>O total da soma é : {soma}<h1>')

def divisao(request, n1, n2):
    divisao = n1 / n2
    return HttpResponse(f'<h1>O total da divisão é : {round(divisao)}<h1>')

def subtracao(request, n1, n2):
    subtracao = n1 - n2
    return HttpResponse(f'<h1>O total da subtração é : {subtracao}<h1>')

def multiplicacao(request, n1, n2):
    multiplicacao = n1 * n2
    return HttpResponse(f'<h1>O total da multiplicação é: {multiplicacao}</h1>')