from datetime import datetime
from subprocess import (call)
from telegram.ext import (CommandHandler)
from password import (CODE)
from telegram import ChatAction


def send_screenshot(bot, update, args):
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


def send_camerashot(bot, update, args):
    if len(args) == 0 or args[0] != CODE:
        bot.send_chat_action(chat_id=update.message.chat_id,
                             action=ChatAction.TYPING)

        bot.send_message(chat_id=update.message.chat_id,
                         text="You are not authorized to use this command")
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


def send_network_information(bot, update, args):
    print "fetching network info"


SEND_SCREENSHOT_HANDLER = CommandHandler(
    'screenshot', send_screenshot, pass_args=True)
SEND_CAMERASHOT_HANDLER = CommandHandler(
    'camerashot', send_camerashot, pass_args=True)
