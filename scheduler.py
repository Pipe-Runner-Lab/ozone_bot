def schedule(job_queue, callback, chat_id, args):
    job_queue.run_once(callback, args[0], context=[chat_id, args])
