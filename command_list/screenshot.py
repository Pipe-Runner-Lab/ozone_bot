from subprocess import (call)
from datetime import datetime
from telegram import ChatAction
from telegram.ext import (CommandHandler)
from password.password import CODE


class Screenshot(object):
    def __init__(self):
        self.SEND_SCREENSHOT_HANDLER = CommandHandler(
            'screenshot', self.send_screenshot, pass_args=True)

    def send_screenshot(self, bot, update, args):
        if len(args) == 0 or args[0] != CODE:
            bot.send_chat_action(chat_id=update.message.chat_id,
                                 action=ChatAction.TYPING)

            bot.send_message(chat_id=update.message.chat_id,
                             text="You are not authorized to use this command")
        else:
            bot.send_chat_action(chat_id=update.message.chat_id,
                                 action=ChatAction.UPLOAD_PHOTO)

            call(["import", "-window", "root", "./image/temp.jpg"])
            photo = open("./image/temp.jpg", 'rb')
            bot.send_photo(chat_id=update.message.chat_id,
                           caption=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                           photo=photo)
            call(['rm', '-rf', './image/temp.jpg'])
