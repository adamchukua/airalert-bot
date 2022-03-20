from telethon import TelegramClient, events
from secret import api_id, api_hash, TOKEN, group_id
import telebot

client = TelegramClient('app', api_id, api_hash)
bot = telebot.TeleBot(TOKEN)

@client.on(events.NewMessage(chats=('air_alert_ua')))
async def normal_handler(event):
    message = event.message.to_dict()['message']
    if '#м_Миколаїв_та_Миколаївська_територіальна_громада' or '#Миколаївська_область' in message and '🔴' in message:
        bot.send_photo(group_id, open('img.jpg', 'rb'))

client.start()
client.run_until_disconnected()
bot.infinity_polling()
