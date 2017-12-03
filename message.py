from telegram.ext import (MessageHandler)
from telegram.ext.filters import (Filters)


def message(bot, update):

    photo_object = update.message.photo[-1]
    print photo_object.file_size
    photo_id = photo_object.file_id
    telegram_file = bot.getFile(photo_id)
    telegram_file.download(custom_path='./screenshot/downloadtemp')


MESSAGE = MessageHandler(Filters.photo, message)
