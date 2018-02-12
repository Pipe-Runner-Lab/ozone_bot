def reminder(bot, job):
    bot.send_message(
        chat_id=job.context["chat_id"], text=job.context["message"])
