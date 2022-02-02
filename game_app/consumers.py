from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Room
from channels.db import database_sync_to_async


class GameRoom(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = 'room_%s' % self.room_name
        print(self.room_group_name)
        self.users_count = await self.get_room_users(self.room_name)
        await self.connect_user(self.room_name)
        print(f"connected users in room ......{self.users_count}")
        if self.users_count >= 2:
            await self.close()
        else:
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()

    async def disconnect(self, close_code):
        print(self.room_name)
        await self.disconnect_user(self.room_name)
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        user = self.scope['user']
        text_data_json['user'] = self.scope["user"].username
        print(user)
        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'run_game',
                'Move': json.dumps(text_data_json)
            }
        )

    async def run_game(self, event):
        data = event['Move']
        # data = json.loads(data)

        await self.send(text_data=json.dumps({
            'payload': data
        }))

    @database_sync_to_async
    def get_room_users(self, roomcode):
        try:
            room_obj = Room.objects.get(room=roomcode)
            return room_obj.connected_users
        except Room.DoesNotExist:
            return "room not exits"

    @database_sync_to_async
    def connect_user(self, roomcode):
        room_objs = Room.objects.get(room=roomcode)
        connec = int(0 if room_objs.connected_users is None else room_objs.connected_users)
        room_objs.connected_users = connec + 1
        room_objs.save()
        return None

    @database_sync_to_async
    def disconnect_user(self, roomcode):
        room_objs = Room.objects.get(room=roomcode)
        connec = int(0 if room_objs.connected_users is None else room_objs.connected_users)
        room_objs.connected_users = connec - 1
        room_objs.save()
        return None
