import threading
from chat.models import Bot

#This function I have written to store the return statement from threads which stores the data inside queue data structures
def threaded(f, daemon=False):
    #from multiprocessing 
    import queue

    def wrapped_f(q, *args, **kwargs):
        '''this function calls the decorated function and puts the 
        result in a queue'''
        ret = f(*args, **kwargs)
        q.put(ret)

    def wrap(*args, **kwargs):
        '''this is the function returned from the decorator. It fires off
        wrapped_f in a new thread and returns the thread object with
        the result queue attached'''

        q = queue.Queue()

        t = threading.Thread(target=wrapped_f, args=(q,)+args, kwargs=kwargs)
        t.daemon = daemon
        t.start()
        t.result_queue = q        
        return t

    return wrap

@threaded
def history(name_of_query):
    #Here I am taking the data from database and storing them in queue to return query if '!recent' comes in the message content
    recents = Bot.objects.all()
    results = []
    l = len(recents)
    for i in range(l):
        if name_of_query in recents[i].history:
            results.append(recents[i].history)
    if len(results) == 0:
        results.append("No Match")
    return results #str(recents[0].history)
def store_history(message):
    # Here I am storing the google search string in the database
    query = Bot(history = message)#content.lower()[7:])
    #histories.append(message)
    query.save()

