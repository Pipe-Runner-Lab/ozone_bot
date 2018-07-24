from subprocess import (call)
from telegram.ext import (
    CommandHandler)
from telegram import ChatAction
from username.username import USERNAME


class Download(object):

    def __init__(self):
        self.DOWNLOAD_LINK = CommandHandler(
            'download', self.download_link, pass_args=True)

    def download_link(self, bot, update, args):
        message_id = update.message.message_id
        username = update.message.from_user.username

        try:
            if username != USERNAME:
                bot.send_chat_action(chat_id=update.message.chat_id,
                                     action=ChatAction.TYPING)

                message = ("Sorry %s, cannot let you do that..." %
                           update.message.from_user.first_name)
                bot.send_message(chat_id=update.message.chat_id,
                                 text=message)
            else:
                bot.send_chat_action(chat_id=update.message.chat_id,
                                     action=ChatAction.TYPING)

                bot.send_message(chat_id=update.message.chat_id,
                                 reply_to_message_id=message_id,
                                 text="Father, I have started downloading your file. I'll let you know when I am done.")
                link = args[0]
                return_code = call(
                    ['aria2c', '-x', '16', link, '-d', './download/'])

                if return_code != 0:
                    bot.send_chat_action(chat_id=update.message.chat_id,
                                         action=ChatAction.TYPING)

                    bot.send_message(chat_id=update.message.chat_id,
                                     reply_to_message_id=message_id,
                                     text="Father, there seems to be some problem, sorry.")
                else:
                    bot.send_chat_action(chat_id=update.message.chat_id,
                                         action=ChatAction.TYPING)

                    bot.send_message(chat_id=update.message.chat_id,
                                     reply_to_message_id=message_id,
                                     text="Father, your file has been downloaded.")
        except IndexError:
            bot.send_chat_action(chat_id=update.message.chat_id,
                                 action=ChatAction.TYPING)

            bot.send_message(chat_id=update.message.chat_id,
                             reply_to_message_id=message_id,
                             text="I don't have enough information to download this file")
