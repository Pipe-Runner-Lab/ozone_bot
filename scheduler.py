def schedule(job_queue, callback, chat_id, args):
    job_queue.run_once(callback, 5, context=[chat_id, args])
