import json
from .parser.usd_parser import usd_parser
from channels.generic.websocket import AsyncWebsocketConsumer
import datetime
from asyncio import sleep


class WSCons(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            await self.send(json.dumps({'message': str(datetime.datetime.now().strftime('%H:%M'))}))
            await sleep(60)


class WSConsUSD(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            usd = json.dumps({'message': str(usd_parser())})
            await self.send(usd)
            await sleep(60)
