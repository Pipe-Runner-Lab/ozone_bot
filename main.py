import logging

# importing token from token file ( not public )
# from key import (token)

# importing from telegram.ext package
from telegram.ext import (Updater)

# importing token
from key import (TOKEN)

# importing custom command modules
from start_command import (START_HANDLER)


def main():
    print("--------- Starting Ozone bot now -------------")

    # logging text message on terminal
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    # creating Updater instance
    updater = Updater(token=TOKEN)

    # creating a dispatcher instance
    dispatcher = updater.dispatcher

    # adding commands to dispatcher
    dispatcher.add_handler(START_HANDLER)

    # starting polling
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
