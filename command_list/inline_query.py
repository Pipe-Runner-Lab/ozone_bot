"""A CFH module to answer to inline queries"""

from telegram import ChatAction
from telegram.ext import InlineQueryHandler


class InlineQuery(object):
    def __init__(self):
        self.INLINE_QUERY_HANDLER = InlineQueryHandler(self.inline_query)
        pass

    def inline_query(self, bot, update):
        query = update.inline_query.query
        print('---------------------')
        print(query)
        return []
