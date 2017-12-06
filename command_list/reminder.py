from subprocess import (call)
from datetime import datetime
from telegram.ext import (
    CommandHandler, ConversationHandler, MessageHandler, CallbackQueryHandler)
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)
from telegram import ChatAction
from utility_job import timer_job
from scheduler import schedule
from telegram.ext.filters import (Filters)
import dateparser


class Reminder(object):
    def __init__(self):
        self.SET_REMINDER = ConversationHandler(
            entry_points=[CommandHandler(
                'set_reminder', self.set_reminder_start, pass_user_data=True)],
            states={
                "SET_REMINDER_DATETIME": [MessageHandler(Filters.text,
                                                         self.set_reminder_datetime,
                                                         pass_user_data=True)],
                "SET_REMINDER_MESSAGE": [MessageHandler(Filters.text,
                                                        self.set_reminder_message,
                                                        pass_job_queue=True,
                                                        pass_user_data=True)],
                "SET_REMINDER_BROADCASE_OPTION": []
            },
            fallbacks=[]

        )

        self.CANCEL_REMINDER = CallbackQueryHandler(
            self.cancel_reminder, pass_user_data=True)

    def set_reminder_start(self, bot, update, user_data):
        bot.send_chat_action(chat_id=update.message.chat_id,
                             action=ChatAction.TYPING)

        keyboard = [[InlineKeyboardButton(
            "Cancel", callback_data="CANCEL_REMINDER")]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        message_id = update.message.message_id
        user_data['message_id'] = message_id
        bot.send_message(chat_id=update.message.chat_id,
                         reply_to_message_id=message_id,
                         text="What time should I remind you?",
                         reply_markup=reply_markup)
        return "SET_REMINDER_DATETIME"

    def set_reminder_datetime(self, bot, update, user_data):
        bot.send_chat_action(chat_id=update.message.chat_id,
                             action=ChatAction.TYPING)

        keyboard = [[InlineKeyboardButton(
            "Cancel", callback_data="CANCEL_REMINDER")]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        date = dateparser.parse(update.message.text)
        message_id = update.message.message_id
        if date != None:
            user_data['date'] = date
            bot.send_message(chat_id=update.message.chat_id,
                             text="What is it about?",
                             reply_markup=reply_markup
                             )

            return "SET_REMINDER_MESSAGE"
        elif date < datetime.now():
            bot.send_message(chat_id=update.message.chat_id,
                             reply_to_message_id=message_id,
                             text="I wish I could go in the past to remind you but I can't... How about we set a correct time one now...",
                             reply_markup=reply_markup)
            return "SET_REMINDER_DATETIME"
        else:
            bot.send_message(chat_id=update.message.chat_id,
                             reply_to_message_id=message_id,
                             text="Sorry, I could not understand this. Please simplify it for me...",
                             reply_markup=reply_markup)
            return "SET_REMINDER_DATETIME"

    def set_reminder_message(self, bot, update, user_data, job_queue):
        bot.send_chat_action(chat_id=update.message.chat_id,
                             action=ChatAction.TYPING)

        user_data['message'] = update.message.text
        date_string = user_data['date'].strftime('%a %d-%m-%Y %I:%M %p')
        bot.send_message(chat_id=update.message.chat_id,
                         text=("I have set your reminder. I will send you a text on %s",
                               date_string))

        return ConversationHandler.END

    def cancel_reminder(self, bot, update, user_data):
        query = update.callback_query

        bot.send_chat_action(chat_id=query.message.chat_id,
                             action=ChatAction.TYPING)

        message_id = user_data['message_id']
        bot.send_message(chat_id=query.message.chat_id,
                         reply_to_message_id=message_id, text="May be next time...")

        user_data.clear()

        return ConversationHandler.END
