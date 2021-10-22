from telethon import TelegramClient, events, sync
from dotenv import load_dotenv
import os

# api credentials
load_dotenv('.env')

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
username = os.getenv("USERNAME")

client = TelegramClient('pextilis', api_id, api_hash)
client.start()

client.send_message(username, 'Hello! Talking to you from Telethon')
