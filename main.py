import logging

# importing from telegram.ext package
from telegram.ext import (Updater)

# importing token
from key import (TOKEN)

# importing custom command modules
from start_command import (START_HANDLER)
from security_command import (SEND_SCREENSHOT_HANDLER, SEND_CAMERASHOT_HANDLER)


def main():
    print("--------- Starting Ozone bot now -------------")

    # logging text message on terminal
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    # creating Updater instance
    updater = Updater(token=TOKEN)

    # creating a dispatcher instance
    dispatcher = updater.dispatcher

    # adding handlers to dispatcher
    dispatcher.add_handler(START_HANDLER)
    dispatcher.add_handler(SEND_SCREENSHOT_HANDLER)
    dispatcher.add_handler(SEND_CAMERASHOT_HANDLER)

    # starting polling
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
