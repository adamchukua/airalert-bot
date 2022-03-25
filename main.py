import os
import random

import telebot
from telethon import TelegramClient, events

from secret import api_id, api_hash, TOKEN, group_id

client = TelegramClient('app_v1', api_id, api_hash)
bot = telebot.TeleBot(TOKEN)


@client.on(events.NewMessage(chats='air_alert_ua'))
async def alert_handler(event):
    message = event.message.to_dict()['message']
    if '#м_Миколаїв_та_Миколаївська_територіальна_громада' in message or '#Миколаївська_область' in message:
        if '🔴' in message:
            media = random.choice(os.listdir('media/alert_on/'))
            if media[-3:] == 'jpg':
                bot.send_photo(group_id, open('media/alert_on/' + media, 'rb'), caption='‍Увага! Повітряна тривога!')
            else:
                bot.send_video(group_id, open('media/alert_on/' + media, 'rb'), caption='‍Увага! Повітряна тривога!')
        elif '🟢' in message:
            media = random.choice(os.listdir('media/alert_off/'))
            if media[-3:] == 'jpg':
                bot.send_photo(group_id, open('media/alert_off/' + media, 'rb'), caption='Увага! Відбій повітряної тривоги!')
            else:
                bot.send_video(group_id, open('media/alert_off/' + media, 'rb'), caption='Увага! Відбій повітряної тривоги!')
    else:
        print(f'{message[2:7]}: bot is working')

client.start()
client.run_until_disconnected()
bot.infinity_polling()
