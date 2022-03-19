from telethon import TelegramClient, events
from secret import api_id, api_hash, TOKEN
import telebot

client = TelegramClient('hp_ubuntu', api_id, api_hash)
bot = telebot.TeleBot(TOKEN)

@client.on(events.NewMessage(chats=('fuufudkye'))) # air_alert_ua
async def normal_handler(event):
    message = event.message.to_dict()['message']
    if '#м_Миколаїв_та_Миколаївська_територіальна_громада' in message and '🔴' in message:
        bot.send_message(-686742350, "Тривога!")

client.start()
client.run_until_disconnected()
bot.infinity_polling()
