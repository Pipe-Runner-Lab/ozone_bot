from subprocess import (call)
from datetime import datetime
from telegram.ext import (
    CommandHandler, ConversationHandler, RegexHandler, MessageHandler, CallbackQueryHandler)
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)
from telegram.ext.filters import (Filters)
from telegram import ChatAction
from utility_job import timer_job
from scheduler import schedule
from password import CODE
import dateparser


def set_reminder_start(bot, update, user_data):
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


def set_reminder_datetime(bot, update, user_data):
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


def set_reminder_message(bot, update, user_data):
    bot.send_chat_action(chat_id=update.message.chat_id,
                         action=ChatAction.TYPING)

    user_data['message'] = update.message.text
    date_string = user_data['date'].strftime('%a %d-%m-%Y %I:%M %p')
    bot.send_message(chat_id=update.message.chat_id,
                     text=("I have set your reminder. I will send you a text on %s",
                           date_string))

    return ConversationHandler.END


def cancel_reminder(bot, update, user_data):
    query = update.callback_query

    bot.send_chat_action(chat_id=query.message.chat_id,
                         action=ChatAction.TYPING)

    message_id = user_data['message_id']
    bot.send_message(chat_id=query.message.chat_id,
                     reply_to_message_id=message_id, text="May be next time...")

    user_data.clear()

    return ConversationHandler.END


def download_link(bot, update, args):
    message_id = update.message.message_id
    try:
        if args[1] != CODE:
            bot.send_message(chat_id=update.message.chat_id,
                             text="You are not authorized to use this command")
        else:
            bot.send_message(chat_id=update.message.chat_id,
                             reply_to_message_id=message_id,
                             text="Father, I have started downloading your file. I'll let you know when I am done.")
            link = args[0]
            return_code = call(
                ['aria2c', '-x', '16', link, '-d', './download/'])

            if return_code != 0:
                bot.send_message(chat_id=update.message.chat_id,
                                 reply_to_message_id=message_id,
                                 text="Father, there seems to be some problem, sorry.")
            else:
                bot.send_message(chat_id=update.message.chat_id,
                                 reply_to_message_id=message_id,
                                 text="Father, your file has been downloaded.")
    except IndexError:
        bot.send_message(chat_id=update.message.chat_id,
                         reply_to_message_id=message_id,
                         text="I don't have enough information to download this file")


SET_REMINDER = ConversationHandler(
    entry_points=[CommandHandler(
        'set_reminder', set_reminder_start, pass_user_data=True)],
    states={
        "SET_REMINDER_DATETIME": [MessageHandler(Filters.text,
                                                 set_reminder_datetime,
                                                 pass_user_data=True)],
        "SET_REMINDER_MESSAGE": [MessageHandler(Filters.text,
                                                set_reminder_message,
                                                pass_job_queue=True,
                                                pass_user_data=True)],
        "SET_REMINDER_BROADCASE_OPTION": []
    },
    fallbacks=[]

)
CANCEL_REMINDER = CallbackQueryHandler(cancel_reminder, pass_user_data=True)
DOWNLOAD_LINK = CommandHandler('download', download_link, pass_args=True)
