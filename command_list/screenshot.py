from subprocess import (call)
from datetime import datetime
from telegram import ChatAction
from telegram.ext import (CommandHandler)
from username.username import USERNAME


class Screenshot(object):
    def __init__(self):
        self.SEND_SCREENSHOT_HANDLER = CommandHandler(
            'screenshot', self.send_screenshot)

    def send_screenshot(self, bot, update):
        username = update.message.from_user.username
        if username != USERNAME:
            bot.send_chat_action(chat_id=update.message.chat_id,
                                 action=ChatAction.TYPING)

            message = ("Sorry %s, cannot let you do that..." %
                       update.message.from_user.first_name)
            bot.send_message(chat_id=update.message.chat_id,
                             text=message)
        else:
            bot.send_chat_action(chat_id=update.message.chat_id,
                                 action=ChatAction.UPLOAD_PHOTO)

            call(["import", "-window", "root", "./image/temp.jpg"])
            photo = open("./image/temp.jpg", 'rb')
            bot.send_photo(chat_id=update.message.chat_id,
                           caption=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                           photo=photo)
            call(['rm', '-rf', './image/temp.jpg'])
