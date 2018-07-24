"""This module is used to respond to spam"""

from telegram.ext import (MessageHandler, CallbackQueryHandler)
from telegram import ChatAction
from telegram.ext.filters import (Filters)

class SpamGuard(object):
    def __init__(self):
        self.SPAM_GUARD_HANDLER = MessageHandler(
            Filters.status_update.new_chat_members, self.handleSpamer, pass_user_data=True)

    def handleSpamer(self, bot, update, user_data):
        for user in update.message.new_chat_members:
			if not user.is_bot and len(user.full_name) > 50 and "VX,QQ" in user.full_name:
				bot.kick_chat_member(chat_id=update.message.chat_id, user_id=user.id)
			print( user.full_name + " just joined the group" )