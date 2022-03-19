from telethon import TelegramClient, sync, events
from secret import api_id, api_hash

client = TelegramClient('hp_ubuntu', api_id, api_hash)

@client.on(events.NewMessage(chats=('fuufudkye'))) # air_alert_ua
async def normal_handler(event):
    print(event.message.to_dict()['message'])

client.start()
client.run_until_disconnected()