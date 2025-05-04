from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from app_sala_furiosa.models import Sala, Mensagem 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from supabase import create_client, Client
import json
import os

url = os.getenv("url")
key = os.getenv("key")
supabase: Client = create_client(url, key)

# Create your views here.
def index(requests):
    return render(requests, "index.html")

def login(requests):
    if requests.method == "POST":
        print(requests.POST)
        usuario_ou_email = requests.POST["fnomeacesso"]
        senha = requests.POST["fsenhaacesso"]
        
        try:
            user_obj = User.objects.get(email = usuario_ou_email)
            username = user_obj.username
        except User.DoesNotExist:
            username = usuario_ou_email

        user = authenticate(requests, username = username, password = senha)
        if user is not None:
            auth_login(requests, user)
            return redirect("/chat/")
        else:
            messages.info(requests, "Credenciais inválidas")
            return redirect("/login/")
    else:
        return render(requests, "login.html")

def registro(requests):
    if requests.method == "POST":
        username = requests.POST["fnome"]
        email = requests.POST["femail"]
        senha = requests.POST["fsenha"]
        senha2 = requests.POST["fsenha2"]

        if senha == senha2:
            if User.objects.filter(email = email).exists():
                messages.info(requests, "Email já está em uso")
                return redirect('/registro/')
            elif User.objects.filter(username = username).exists():
                messages.info(requests, "Usuário já está em uso")
                return redirect('/registro/')
            else:
                usuario = User.objects.create_user(username=username, email=email, password=senha)
                usuario.save()
                return redirect("/login/")
        else:
            messages.info(requests, "As senhas não são iguais")
            return redirect("/registro/")
    else:
        return render(requests, "registro.html")   

def sala_view(request, nome_sala):
    return render(request, "sala-nova.html", {"nome_sala": nome_sala})

def chat(request):
    return render(request, "chat.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

@csrf_exempt
def cria_sala(request):
    if request.method == "POST":
        data = json.loads(request.body)
        nome_sala = data.get("nome_sala")
        nome_usuario = data.get("nome_usuario")
        if not nome_sala:
            return JsonResponse({"success": False, "erro": "Nome inválido"}, status=400)
        
        result = supabase.table("Salas").select("*").eq("nome", nome_sala).execute()

        if len(result.data) > 0:
            return JsonResponse({"success": True, "url": f"/chat/{nome_sala}",
                                  "ja_existe": True, "nome_usuario": nome_usuario})
        else:
            insert_result = supabase.table("Salas").insert({"nome": nome_sala}).execute()

            if insert_result.data:  
                return JsonResponse({"success": True, "url": f"/chat/{nome_sala}",
                                      "ja_existe": False, "nome_usuario": nome_usuario})
            else:
                return JsonResponse({"success": False, "erro": "Erro ao criar sala"}, status = 500)