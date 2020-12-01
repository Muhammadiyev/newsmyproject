from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from django.contrib.auth import get_user_model
User = get_user_model()
from channels.db import database_sync_to_async
from .serializers import ChatPostSerializer
import pickle
from .views import get_last_10_messages
from .models import Chat, Room



class ChatConsumer(WebsocketConsumer):

    def fetch_messages(self, data):
        messages = get_last_10_messages(data['chatId'])
        print(messages)
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        user = text_data_json['user']
        self.save_chat(user, message)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room':self.room_name,
                'user':user
            }
        )

    def chat_message(self, event):
        message = event['message']
        username = event['username']
        room_name = event["room"]
        user = event["user"]

        self.send(text_data=json.dumps({
            'message': message,
            'username':username,
            'room':self.room_name,
            'user':user
        }))

    def send_message(self, message):
        self.send(text_data=json.dumps(message))
        
    def save_chat(self, user, message):
        thread_obj = self.room_name
        room = Room.objects.get(id=thread_obj)
        user_id = User.objects.get(id=user)
        chat_all = Chat.objects.create(room=room,user=user_id, text=message)
        chat = Chat.objects.filter(room=room).all()
        return True