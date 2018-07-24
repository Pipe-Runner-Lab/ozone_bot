"""CFH module to spam a group to hide some crucial information"""

from telegram.ext import (
    CommandHandler)
from telegram import ChatAction
from thread import start_new_thread
from random import choice


class Spam(object):
    def __init__(self):
        self.SPAM_START_HANDLER = CommandHandler('spam_start', self.spam_start)
        self.SPAM_STOP_HANDLER = CommandHandler('spam_stop', self.spam_stop)
        self.spam_flag = False
        self.chat_list = set()
        self.chat_text = ['She who arrival end how fertile enabled. Brother she add yet see minuter natural smiling article painted. Themselves at dispatched interested insensible am be prosperous reasonably it.',
                          'In either so spring wished. Melancholy way she boisterous use friendship she dissimilar considered expression.',
                          'Sex quick arose mrs lived. Mr things do plenty others an vanity myself waited to. Always parish tastes at as mr father dining at. ',
                          'Received overcame oh sensible so at an. Formed do change merely to county it. Am separate contempt domestic to to oh. On relation my so addition branched. Put hearing cottage she norland letters equally prepare too. Replied exposed savings he no viewing as up.',
                          'Soon body add him hill. No father living really people estate if. Mistake do produce beloved demesne if am pursuit.',
                          'Is branched in my up strictly remember. Songs but chief has ham widow downs. Genius or so up vanity cannot. Large do tried going about water defer by. Silent son man she wished mother. Distrusts allowance do knowledge eagerness assurance additions to. ',
                          'Too cultivated use solicitude frequently. Dashwood likewise up consider continue entrance ladyship oh. Wrong guest given purse power is no. Friendship to connection an am considered difficulty. ',
                          'Country met pursuit lasting moments why calling certain the. Middletons boisterous our way understood law. Among state cease how and sight since shall. Material did pleasure breeding our humanity she contempt had. So ye really mutual no cousin piqued summer result. ',
                          'Greatly cottage thought fortune no mention he. Of mr certainty arranging am smallness by conveying. Him plate you allow built grave. Sigh sang nay sex high yet door game. She dissimilar was favourable unreserved nay expression contrasted saw. Past her find she like bore pain open',
                          'Shy lose need eyes son not shot. Jennings removing are his eat dashwood. Middleton as pretended listening he smallness perceived. Now his but two green spoil drift. ', ]

    def spam_start(self, bot, update):
        username = update.message.from_user.username
        if username != 'humble_D':
            bot.send_chat_action(chat_id=update.message.chat_id,
                                 action=ChatAction.TYPING)

            message = ("Sorry %s, cannot let you do that..." %
                       update.message.from_user.first_name)
            bot.send_message(chat_id=update.message.chat_id,
                             text=message)
        else:
            self.chat_list.add(update.message.chat_id)

        # start thread only if spammer is not already working
        start_new_thread(self.spammer, (bot, update))

    def spammer(self, bot, update):
        chat_id = update.message.chat_id
        while(chat_id in self.chat_list):
            bot.send_message(chat_id=chat_id,
                             text=choice(self.chat_text))

    def spam_stop(self, bot, update):
        username = update.message.from_user.username
        if username != 'humble_D':
            bot.send_chat_action(chat_id=update.message.chat_id,
                                 action=ChatAction.TYPING)

            bot.send_message(chat_id=update.message.chat_id,
                             text="Nope!!")
        else:
            self.chat_list.remove(update.message.chat_id)
