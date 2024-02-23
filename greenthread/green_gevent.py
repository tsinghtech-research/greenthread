import gevent
from gevent import event
from gevent import pool
from gevent import queue
from gevent.timeout import Timeout

USE_GREEN_BACKEND = 'gevent'

green_sleep = gevent.sleep

green_spawn = gevent.spawn

def green_thread_join(thr):
    return thr.join()

GreenQueue = queue.Queue

GreenPool = pool.Pool

def green_pool_map(pool, *args, **kws):
    return pool.imap(*args, **kws)

def green_pool_join(pool, timeout=None):
    return pool.join(timeout)

class GreenEvent:
    def __init__(self):
        self.ret = event.AsyncResult()

    def ready(self):
        return self.ret.ready()

    def set(self, data):
        self.ret.set(data)

    def get(self, timeout=None):
        block = False if timeout == 0 else True
        return self.ret.get(block=block, timeout=timeout)

def tpool_execute(func, *args, **kws):
    pool = gevent.get_hub().threadpool
    return pool.spawn(func, *args, **kws).get()

class GreenTimeout(Timeout):
    def __init__(self, *args, **kws):
        super().__init__(*args, **kws)
        self.start()

    cancel = Timeout.close
