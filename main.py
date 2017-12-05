import logging
import sqlite3
from telegram.ext import (Updater)
from key import (TOKEN)
from start_command import (START_HANDLER)
from security_command import (SEND_SCREENSHOT_HANDLER, SEND_CAMERASHOT_HANDLER)
from utility_command import (SET_REMINDER, CANCEL_REMINDER, DOWNLOAD_LINK)


def main():
    print("--------- Starting Ozone bot -------------")

    # logging text message on terminal
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    # creating database cursor
    connection = sqlite3.connect('data.db')

    # creating Updater instance
    updater = Updater(token=TOKEN)

    # creating a dispatcher instance
    dispatcher = updater.dispatcher

    # creating job scheduler instance
    # job_queue = updater.job_queue

    # adding handlers to dispatcher
    dispatcher.add_handler(START_HANDLER)
    dispatcher.add_handler(SEND_SCREENSHOT_HANDLER)
    dispatcher.add_handler(SEND_CAMERASHOT_HANDLER)
    dispatcher.add_handler(SET_REMINDER)
    dispatcher.add_handler(CANCEL_REMINDER)
    dispatcher.add_handler(DOWNLOAD_LINK)

    # calling in the scheduler

    # starting polling
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
