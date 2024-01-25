import json
from channels.generic.websocket import AsyncWebsocketConsumer

class PlayerCoordinatesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        try:
            coordinates = json.loads(text_data)

            if isinstance(coordinates, dict):
                x = coordinates.get('x')
                y = coordinates.get('y')

                if x is not None and y is not None:
                    print(f"Received coordinates: x={x}, y={y}")

                else:
                    print("Invalid coordinates format")

            else:
                print("Received data is not a valid JSON object")

        except json.JSONDecodeError:
            print("Invalid JSON format")
