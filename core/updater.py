from time import sleep
from threading import Thread, Lock
from telegram.error import NetworkError, Unauthorized


class Updater:
    def __init__(self, bot=None):
        self.bot = bot
        self._thread = Thread(target=self._update_loop)
        self.running = False
        self.update_id = None
        self.update_callback = None

    def set_callback(self, cb):
        self.update_callback = cb

    def _dispatch_updates(self):
        if self.update_id:
            updates = self.bot.get_updates(self.update_id+1, timeout=10)
        else:
            updates = self.bot.get_updates(timeout=10)
        for update in updates:
            self.update_id = update.update_id
            print('update!', update)
            self.update_callback(update)

    def _update_loop(self):
        while self.running:
            try:
                self._dispatch_updates()
            except NetworkError:
                sleep(1)
            except Unauthorized:
                pass

    def start(self):
        self.running = True
        self._thread.start()
