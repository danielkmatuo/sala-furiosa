from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("login/", views.login, name = "login"),
    path("registro/", views.registro, name = "registro"),
    path("chat/<str:nome_sala>/", views.sala_view, name = "sala_view"),
    path("criar-sala/", views.cria_sala, name = "cria_sala"),
    path("chat/", views.chat, name = "chat"),
    path("logout/", views.logout, name = "logout")
]