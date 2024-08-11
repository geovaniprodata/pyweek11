from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth
# Create your views here.

def cadastro(request):
    if request.user.is_authenticated:
          return redirect('/empresarios/cadastrar_empresa')
    
    if request.method == 'GET':
            return render(request, 'cadastro.html')
    elif request.method == 'POST':
            username = request.POST.get('username')
            senha = request.POST.get('senha')
            confirmar_senha = request.POST.get('confirmar_senha')

            if not senha == confirmar_senha:
                messages.add_message(request, constants.ERROR, 'A senhas não coincidem.')
                return redirect('/usuarios/cadastro')
            
            if len(senha) < 6:
                  messages.add_message(request, constants.ERROR, 'A senha precisa ter pelo menos 6 digitos.')
                  return redirect('/usuarios/cadastro')
            
            temUsers = User.objects.filter(username=username).exists()
            
            if temUsers:
                  messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse Username.')
                  return redirect('/usuarios/cadastro')
            
            user = User.objects.create_user(
                  username=username,
                  password=senha,
            )
            
            return redirect('/usuarios/logar')

def logar(request):
    if request.user.is_authenticated:
          return redirect('/empresarios/cadastrar_empresa')
    
    if request.method == 'GET':
        return render(request, 'logar.html')
    elif request.method == "POST":
          username = request.POST.get('username')
          senha = request.POST.get('senha')

          user = auth.authenticate(request, username=username, password=senha)

          if user:
                auth.login(request, user)
                return redirect('/empresarios/cadastrar_empresa')
          messages.add_message(request, constants.ERROR, "Usuário ou senha inválidos.")
          return redirect('/usuarios/logar')

