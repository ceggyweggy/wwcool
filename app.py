from flask import Flask, request, jsonify
import time 

from telegram_bot import TelegramBot
from config import TELEGRAM_INIT_WEBHOOK_URL

app = Flask(__name__)
TelegramBot.init_webhook(TELEGRAM_INIT_WEBHOOK_URL)

unixtime = int(time.time())

@app.route('/webhook', methods=['POST'])
def index():
    req = request.get_json()
    bot = TelegramBot()
    bot.parse_webhook_data(req)
    success = bot.action()
    return jsonify(success=success) # TODO: Success should reflect the success of the reply

if __name__ == '__main__':
    app.run(port=5000)


# https://telegram.me

# check bot initialization: https://api.telegram.org/bot<BOT_TOKEN>/getme # yes, with the <> brackets 
# check webhook url: https://api.telegram.org/botBOT_TOKEN/getWebhookInfo
