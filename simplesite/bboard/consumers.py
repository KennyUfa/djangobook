import json

from channels.generic.websocket import AsyncWebsocketConsumer
import datetime
from asyncio import sleep


class WSCons(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            await self.send(json.dumps({'message': str(datetime.datetime.now().strftime('%M:%S'))}))
            await sleep(1)
