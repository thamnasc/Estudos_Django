from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello, {}, você tem {} anos</h1>'.format(nome, idade))

def soma(request, numero1, numero2):
    return HttpResponse('<h1>{} + {} = {}</h1>'.format(numero1, numero2,(numero1 + numero2)))

def subtracao(request, numero1, numero2):
    return HttpResponse('<h1>{} - {} = {}</h1>'.format(numero1, numero2, (numero1 - numero2)))

def multiplicacao(request, numero1, numero2):
    return HttpResponse('<h1>{} x {} = {}</h1>'.format(numero1, numero2,(numero1 * numero2)))

def divisao(request, numero1, numero2):
    return HttpResponse('<h1>{} / {} = {}</h1>'.format(numero1, numero2,(numero1 / numero2)))