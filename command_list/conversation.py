"""This module is used to store and respond to normal conversations"""

from telegram.ext import (
    ConversationHandler, MessageHandler, CallbackQueryHandler)
from telegram import ChatAction
from telegram.ext.filters import (Filters)


class Conversation(object):
    def __init__(self):
        self.CHAT_HANDLER = MessageHandler(
            Filters.text, self.chat, pass_user_data=True)

    def chat(self, bot, update, user_data):
        print(update.message.text)
        print(update.message.chat_id)
