from threading import Lock
from core import Updater, WorkerBee

from base import BaseContext


class BotHive:
    def __init__(self, bot):
        self.bot = bot
        self.global_entry = BaseContext()
        self.updater = Updater(bot)
        self.updater.set_callback(self.dispatch_update)
        self.workers = list()
        self.workers_lock = Lock()

    def _new_worker(self):
        w = WorkerBee(self.bot, self.global_entry)
        self.workers.append(w)

    def dispatch_update(self, update):
        # todo replace to some more complicated worker management
        self.workers_lock.acquire()
        if not self.workers:
            self._new_worker()
        self.workers_lock.release()
        self.workers[0].dispatch_update(update)

    def start(self):
        self.updater.start()
        for w in self.workers:
            w.start()

    def monitor(self):
        import time
        while True:
            for w in self.workers:
                print(f'+ ==< {w.id} >==')
                for s in w.sessions:
                    print(f'| {s.id} >=< {[c.id for c in s.contexts]}')
                print('+ ==< {+} >==')
                print('\n\n')
            time.sleep(1)

    def idle(self):
        import time
        while True:
            time.sleep(1)
