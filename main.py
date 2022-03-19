from telethon import TelegramClient, sync, events
from secret import api_id, api_hash

client = TelegramClient('hp_ubuntu', api_id, api_hash)

@client.on(events.NewMessage(chats=('fuufudkye'))) # air_alert_ua
async def normal_handler(event):
    message = event.message.to_dict()['message']
    if '#м_Миколаїв_та_Миколаївська_територіальна_громада' in message and '🔴' in message:
        print('Тривога!')

client.start()
client.run_until_disconnected()