import logging
from telegram.ext import (Updater)
from key.key import (TOKEN)
from command_list.start import (Start)
from command_list.spamGuard import (SpamGuard)

START = Start()
SPAM_GUARD = SpamGuard()

def main():
    print "--------- Starting Ozone bot -------------"

    # logging text message on terminal
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    # creating Updater instance
    updater = Updater(token=TOKEN)

    # creating a dispatcher instance
    dispatcher = updater.dispatcher

    # creating job scheduler instance
    # job_queue = updater.job_queue

    # adding handlers to dispatcher
    dispatcher.add_handler(START.START_HANDLER)
    dispatcher.add_handler(SPAM_GUARD.SPAM_GUARD_HANDLER)

    # starting polling
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
