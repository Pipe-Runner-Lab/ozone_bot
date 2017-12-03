# importing command handler from telegram.ext
from telegram.ext import (CommandHandler)


def reboot():
    print "rebooting"


def shutdown():
    print "shutting down"


def lock():
    print "locking"
