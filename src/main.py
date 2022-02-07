from telethon import TelegramClient, events, sync
from dotenv import load_dotenv
import os

def auth_data(file_name: str) -> dict:
    '''
    take a file and grab all needed
    credentials to use telethon
    '''

    # api credentials
    load_dotenv(file_name)

    auth_keys = {
        'api_id': os.getenv("API_ID"),
        'api_hash': os.getenv("API_HASH"),
        'username': os.getenv("USERNAME")
    }

    return auth_keys

auth_keys = auth_data('.env')

client = TelegramClient('pextilis', auth_keys['api_id'], auth_keys['api_hash'])
client.start()

client.send_message(auth_keys['username'], 
    'Hello! Talking to you from Telethon')
