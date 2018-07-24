from telegram import ChatAction
from telegram.ext import (CommandHandler)
from database.Database_utility import (Database_utility)


class DeleteUsers(object):
    def __init__(self):
        self.DELETE_USERS_HANDLER = CommandHandler(
            'deleteusers', self.delete_users, pass_args=True)

    def delete_users(self, bot, update, args):
        db = Database_utility()
        db.delete_user_data()

        bot.send_chat_action(chat_id=update.message.chat_id,
                             action=ChatAction.TYPING)

        bot.send_message(chat_id=update.message.chat_id,
                         text="Flashed my memory")
