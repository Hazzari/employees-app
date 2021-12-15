import asyncio

from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

from app.core.config import MONGO_DB_URL

client = AsyncIOMotorClient(MONGO_DB_URL)
client.get_io_loop = asyncio.get_event_loop
engine = AIOEngine(motor_client=client)
