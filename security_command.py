# importing command handler from telegram.ext
from telegram.ext import (CommandHandler)

# importing the subprocess module
from subprocess import (call)

# importing date time
from datetime import datetime


def send_screenshot(bot, update):
    call(["import", "-window", "root", "./screenshot/temp.jpg"])
    photo = open("./screenshot/temp.jpg", 'rb')
    bot.send_photo(chat_id=update.message.chat_id,
                   caption=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                   photo=photo)
    call(['rm', '-rf', './screenshot/temp.jpg'])


def send_camerashot(bot, update):
    call(['fswebcam', '-r', '1600x1200', '--jpeg', '-1', '-D', '0',
          '-S', '15', '--no-banner', './screenshot/camera_temp.jpg'])
    photo = open("./screenshot/camera_temp.jpg", 'rb')
    bot.send_photo(chat_id=update.message.chat_id,
                   caption=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                   photo=photo)
    call(['rm', '-rf', './screenshot/camera_temp.jpg'])


SEND_SCREENSHOT_HANDLER = CommandHandler('screenshot', send_screenshot)
SEND_CAMERASHOT_HANDLER = CommandHandler('camerashot', send_camerashot)
