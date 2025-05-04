import json
from channels.generic.websocket import AsyncWebsocketConsumer
from supabase import Client, create_client
import os
from channels.db import database_sync_to_async
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("url")
key = os.getenv("key")
supabase: Client = create_client(url, key)

class SalaFuriosaConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def salva_supabase(self, data):
        return supabase.table("Mensagens").insert(data).execute()
    
    @database_sync_to_async
    def pega_mensagem(self, nome_sala):
        response = supabase.table("Mensagens").select("*").eq("sala", nome_sala).order("criada_dia").order("criada_hora").execute()
        return response.data

    async def connect(self):
        # Esse método é chamado quando a conexão WebSocket é estabelecida
        self.room_name = self.scope["url_route"]["kwargs"]["nome_sala"]
        self.room_group_name = f"chat_{self.room_name}"
        self.usuario = self.scope["user"].username

        # Criação de uma sala e conexão ao grupo WebSocket
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Aceita a conexão WebSocket
        await self.accept()

        mensagens = await self.pega_mensagem(self.room_name)

        for msg in mensagens:
            await self.send(text_data = json.dumps({
                "message": msg["msg"],
                "usuario": msg["sender"],
                "horario": msg["criada_hora"]
            }))

    async def disconnect(self, close_code):
        # Esse método é chamado quando a conexão WebSocket é fechada
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Esse método é chamado quando uma mensagem é recebida do WebSocket
        print("dados recebidos:", text_data)
        
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        dias = text_data_json["day_month"]
        horas = text_data_json["hours"]

        await self.salva_supabase({
            "sender": self.usuario,
            "msg": message,
            "sala": self.room_name,
            "criada_dia": dias,
            "criada_hora": horas
        })

        # Enviar a mensagem para o grupo de sala
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                "username": self.usuario,
                "hours": horas
            }
        )

    async def chat_message(self, event):
        # Esse método é chamado quando uma mensagem é enviada ao grupo
        message = event['message']
        usuario = event["username"]
        horario = event["hours"]

        # Enviar a mensagem para o WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            "usuario": usuario,
            "horario": horario
        }))