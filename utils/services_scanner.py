from bleak import BleakClient
from bleak import BleakScanner
import asyncio

async def inspect():
    devices = await BleakScanner.discover()
    device = next(d for d in devices if d.name == "Pybricks Hub")
    async with BleakClient(device) as client:
        for service in client.services:
            print(service)
            for char in service.characteristics:
                print("  ", char.uuid, char.properties)
asyncio.run(inspect())