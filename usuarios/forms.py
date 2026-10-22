from django import forms

class cadastroForms(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.CharField(label='E-mail')
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    confirmar_senha = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)