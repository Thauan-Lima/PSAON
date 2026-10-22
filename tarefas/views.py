from django.shortcuts import render

def dashboard(request):
    return render(request,'tarefas/dashboard.html')

def criar_tarefa(request):
    return render(request,'tarefas/criar_tarefa.html')