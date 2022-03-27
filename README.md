# myko_airalert_bot
## How to get started
Для початку використання бота потрібно:
1) cкопіювати репозиторій https://github.com/TheGradle/myko_airalert_bot;
2) встановити python3 та бібліотеки pip: telebot, telethon;
3) cтворити файли <code>secret.py</code> та <code>subscribers.txt</code> (тут містяться chat_id користувачів та/або груп, яким відправлятимуться сповіщення, можете залишити пустим). Файлі secret.py має бути вигляду:
<pre><code>api_id = 11111111
api_hash = 'ababababab'
TOKEN = '11111111:abaBAbabab'
</code></pre>
<code>api_id</code> та <code>api_hash</code> отримайте створивши Telegram Application, детальніше <a href="https://core.telegram.org/api/obtaining_api_id" target="_blank">тут</a><br>
<code>TOKEN</code> отримайте створивши Telegram-бота, детальніше <a href="https://core.telegram.org/bots" target="_blank">тут</a>
<br>4) запустити файл <code>main.py</code> та автентифікуватись через свій акаунт Telegram.
