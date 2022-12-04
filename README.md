# airalert-bot

## How to get started

You can use the following bot: https://t.me/myko_airalert_bot, or start on your machine:

1. Download and install GIT (https://git-scm.com/downloads).
2. Download and install Python (https://www.python.org/downloads/).
3. Open cmd.exe with admin privileges, change directory for that one (<code>cd [path]</code>), where you want to install the project, and clone this repository with next command: <code>git clone https://github.com/thegradle/airalert-bot</code>
4. Type in command line: <code>cd airalert-bot</code>
5. Install pyTelegramBotAPI with next command: <code>pip3 install pyTelegramBotAPI</code>
6. Install Telethon with next command: <code>pip3 install telethon</code>
7. Create files <code>secret.py</code> and <code>subscribers.txt</code>. Type in the <code>secret.py</code>:
<pre><code>api_id = 11111111
api_hash = 'ababababab'
TOKEN = '11111111:abaBAbabab'
</code></pre>
<code>api_id</code> and <code>api_hash</code> you can get if create Telegram Application, https://core.telegram.org/api/obtaining_api_id<br>
<code>TOKEN</code> is token of your bot given by @botfather (https://sendpulse.com/knowledge-base/chatbot/telegram/create-telegram-chatbot)
8. Start the bot by following code: <code>python3 main.py</code>

#### "ModuleNotFoundError: No module named 'telebot'" problem solved there https://stackoverflow.com/questions/58121141/how-to-fix-importerror-no-module-named-telebot
