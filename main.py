import logging
from telegram.ext import (Updater)
from key import (TOKEN)
from start_command import (START_HANDLER)
from security_command import (SEND_SCREENSHOT_HANDLER, SEND_CAMERASHOT_HANDLER)
from utility_command import (SET_TIMER)
from message import (MESSAGE)


def main():
    print("--------- Starting Ozone bot -------------")

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
    dispatcher.add_handler(START_HANDLER)
    dispatcher.add_handler(SEND_SCREENSHOT_HANDLER)
    dispatcher.add_handler(SEND_CAMERASHOT_HANDLER)
    dispatcher.add_handler(SET_TIMER)
    dispatcher.add_handler(MESSAGE)

    # calling in the scheduler

    # starting polling
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
