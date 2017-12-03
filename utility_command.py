from telegram.ext import (CommandHandler)
from utility_job import timer_job
from scheduler import schedule


def timer(bot, update, job_queue, args):
    bot.send_message(chat_id=update.message.chat_id, text=(
        "Your timer has been set for %s" % args[0]))

    schedule(job_queue, timer_job, update.message.chat_id, args)


SET_TIMER = CommandHandler('timer', timer, pass_args=True, pass_job_queue=True)
