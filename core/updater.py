from time import sleep
from threading import Thread, Lock
from telegram.error import NetworkError, Unauthorized


class Updater:
    def __init__(self, bot=None):
        self.bot = bot
        self._thread = Thread(target=self._update_loop)
        self.running = False
        self.update_id = None

    def _dispatch_updates(self):
        for update in self.bot.get_updates(self.update_id+1, timeout=10):
            self.update_id = update.update_id

    def _update_loop(self):
        while self.running:
            try:
                self._dispatch_updates()
            except NetworkError:
                sleep(1)
            except Unauthorized:
                pass
