from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import User, Message
from django.shortcuts import get_object_or_404

user_list = ['sudeep']

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
    
        await self.accept()
        #connected = json.loads(self.scope['protocols'])
        #user_list.append(connected)
        #await self.receive()

        user_list.append()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': None,
                'user': None,
                'online': user_list
            }
        )

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json['message']:
            message = text_data_json['message']
            user = text_data_json['user']
            text = Message.objects.create(user=get_object_or_404(User, user_name=user), message=message)
            user = text.user.user_name
        else:
            message = None
            user = None
        if not text_data_json['user'] in user_list:
            user_list.append(text_data_json['user'])

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user,
                'online': user_list
            }
        )
    
    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        online = event['online']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
            'online': online
        }))


#class OnlineConsumer(AsyncWebsocketConsumer):

#    async def connect (self):
#        self.room_name = self.scope['url_route']['kwargs']['room_name']
#        self.room_group_name = 'chat_%s' % self.room_name

#        await self.channel_layer.group_add(
#            self.room_group_name,
#            self.channel_name
#        )

#        await self.accept()
    
#    async def receive (self, text_data):
#        text_data_json = json.loads(text_data)
#        connected = text_data_json['online_user']
#        user_list.append(connected)
#        await self.channel_layer.group_send(
#            self.room_group_name,
#            {
#                'type': 'user_connected',
#                'connected': user_list
#            }
#        )

    
#    async def disconnect (self):
#        await self.channel_layer.group_discard(
#            self.room_group_name,
#            self.channel_name
#        )
    
#    async def user_connected (self, event):
#        users = event['connected']

#        await self.send(text_data=json.dumps({
#            'connected': users
#        }))