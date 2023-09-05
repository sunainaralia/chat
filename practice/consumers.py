from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
import json
import asyncio
from asgiref.sync import async_to_sync
from .models import ChatModel,GroupModel
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        self.groupname=self.scope['url_route']['kwargs']['groupkaname']
        user=self.scope['user']
        self.room=f'{self.groupname}{user}'
        group=GroupModel.objects.filter(name=self.room).first()
        if group:
            data=ChatModel.objects.filter(group=group.id)
        else:
            groups=GroupModel(name=self.room)
            groups.save()
        async_to_sync(self.channel_layer.group_add)(self.room,self.channel_name)
        self.send({
            'type':'websocket.accept'
        })
    def websocket_receive(self,event):
        data=json.loads(event['text'])
        group=GroupModel.objects.get(name=self.room)
        if self.scope['user'].is_authenticated:
            chat=ChatModel(content=data['msg'],group=group)
            chat.save()
            data['user']=self.scope['user'].username
            async_to_sync(self.channel_layer.group_send)(self.groupname,{
                'type':'chat.message',
                'message':json.dumps(data)
            })
        else:
            self.send({
                'type':'websocket.send',
                'text':json.dumps({'msg':'login is required','user':'guest'})
            })
    def chat_message(self,event):
        self.send({
            'type':'websocket.send',
            'text':event['message']
        })
    def websocket_disconnect(self,event):
        async_to_sync(self.channel_layer.group_discard)(self.groupname,self.channel_name)
        raise StopConsumer()
