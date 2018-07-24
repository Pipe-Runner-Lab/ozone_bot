from subprocess import (call)
from datetime import datetime
from telegram import ChatAction
from telegram.ext import (CommandHandler)
from username.username import USERNAME


class Camerashot(object):
    def __init__(self):
        self.SEND_CAMERASHOT_HANDLER = CommandHandler(
            'camerashot', self.send_camerashot)

    def send_camerashot(self, bot, update):
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

            call(['fswebcam', '-r', '1600x1200', '--jpeg', '-1', '-D', '0',
                  '-S', '15', '--no-banner', './image/camera_temp.jpg'])
            photo = open("./image/camera_temp.jpg", 'rb')
            bot.send_photo(chat_id=update.message.chat_id,
                           caption=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                           photo=photo)
            call(['rm', '-rf', './image/camera_temp.jpg'])
