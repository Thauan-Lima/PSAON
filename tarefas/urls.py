from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('nova/',views.criar_tarefa, name='criar_tarefa'),
]
