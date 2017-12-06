import logging
import sqlite3
from telegram.ext import (Updater)
from key.key import (TOKEN)
from command_list.start import (Start)
from command_list.camerashot import (Camerashot)
from command_list.screenshot import (Screenshot)
from command_list.reminder import (Reminder)
from command_list.download import (Download)

START = Start()
CAMERASHOT = Camerashot()
SCREENSHOT = Screenshot()
REMINDER = Reminder()
DOWNLOAD = Download()


def main():
    print "--------- Starting Ozone bot -------------"

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
    dispatcher.add_handler(START.START_HANDLER)
    dispatcher.add_handler(SCREENSHOT.SEND_SCREENSHOT_HANDLER)
    dispatcher.add_handler(CAMERASHOT.SEND_CAMERASHOT_HANDLER)
    dispatcher.add_handler(REMINDER.SET_REMINDER)
    dispatcher.add_handler(REMINDER.CANCEL_REMINDER)
    dispatcher.add_handler(DOWNLOAD.DOWNLOAD_LINK)

    # calling in the scheduler

    # starting polling
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
