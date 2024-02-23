import eventlet
from eventlet import tpool
from eventlet.queue import LightQueue
from eventlet.timeout import Timeout

USE_GREEN_BACKEND = "eventlet"

green_sleep = eventlet.sleep

green_spawn = eventlet.spawn

def green_thread_join(thr):
    return thr.wait()

GreenQueue = LightQueue

GreenPool = eventlet.GreenPool

def green_pool_map(pool, *args, **kws):
    return pool.imap(*args, **kws)

def green_pool_join(pool, timeout=None):
    return pool.waitall()

class GreenEvent:
    def __init__(self):
        self.evt = eventlet.Event()

    def ready(self):
        return self.evt.ready()

    def set(self, data):
        self.evt.send(data)

    def get(self, timeout=None):
        return self.evt.wait(timeout)

def tpool_execute(func, *args, **kws):
    return tpool.execute(func, *args, **kws)

class GreenTimeout(Timeout):
    close = Timeout.cancel
