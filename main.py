from telethon import TelegramClient, events
from secret import api_id, api_hash, TOKEN, group_id
import telebot

client = TelegramClient('app_v1', api_id, api_hash)
bot = telebot.TeleBot(TOKEN)


@client.on(events.NewMessage(chats='air_alert_ua'))
async def alert_handler(event):
    message = event.message.to_dict()['message']
    if '#м_Миколаїв_та_Миколаївська_територіальна_громада' in message or '#Миколаївська_область' in message:
        if '🔴' in message:
            bot.send_photo(group_id, open('media/alert_on/1.jpg', 'rb'), caption='‍Увага! Повітряна тривога!')
        elif '🟢' in message:
            bot.send_photo(group_id, open('media/alert_off/1.jpg', 'rb'), caption='Увага! Відбій повітряної тривоги!')


client.start()
client.run_until_disconnected()
bot.infinity_polling()
