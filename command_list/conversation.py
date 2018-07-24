"""This module is used to store and respond to normal conversations"""

from telegram.ext import (
    ConversationHandler, MessageHandler, CallbackQueryHandler)
from telegram import ChatAction
from telegram.ext.filters import (Filters)
from database.Database_utility import (Database_utility)


class Conversation(object):
    def __init__(self):
        self.CHAT_HANDLER = MessageHandler(
            Filters.text, self.chat, pass_user_data=True)

    def chat(self, bot, update, user_data):
        db = Database_utility()

        user_id = update.message.from_user.id
        username = update.message.from_user.username

        search_result = db.get_user_data(user_id)

        if search_result is None:
            message = ("Hi %s, seems like we haven't met before. I have added you to my database!" %
                       update.message.from_user.first_name)
            db.insert_user_data(user_id, username)
            bot.send_message(chat_id=update.message.chat_id,
                             text=message)
        else:
            print search_result
            pass
        print(update.message.text)
        print(user_id)
