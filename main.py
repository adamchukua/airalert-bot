from telethon import TelegramClient, sync
from secret import api_id, api_hash

client = TelegramClient('hp_ubuntu', api_id, api_hash)
client.start()