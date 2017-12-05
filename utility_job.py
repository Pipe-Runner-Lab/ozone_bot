def timer_job(bot, job):
    bot.send_message(chat_id=job.context[0], text=job.context[1][1])
