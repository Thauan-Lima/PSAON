from django.shortcuts import render, redirect

def login(request):
    return render(request, 'usuarios/login.html')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def inicio(request):
    return render(request, 'tarefas/listar_tarefas.html')
