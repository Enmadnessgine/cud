import json
from channels.generic.websocket import AsyncWebsocketConsumer

class PlayerCoordinatesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        x = text_data_json['x']
        y = text_data_json['y']

        print(f"Received coordinates: x={x}, y={y}")