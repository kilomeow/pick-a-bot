from abstraction import Worker
from meta import HashIdentifiable

from core import ChatSession

import asyncio
from threading import Thread


class WorkerBee(Worker, metaclass=HashIdentifiable):
    def __init__(self, bot, global_entry=None):
        self.bot = bot
        self.global_entry = global_entry
        self.loop = asyncio.new_event_loop()
        self._t = Thread(target=self.loop.run_forever)
        self.sessions_dict = dict()

    def _new_session(self, chat_id):
        s = ChatSession(self, self.bot, chat_id)
        self.sessions[chat_id] = s
        return s

    def dispatch_update(self, update):
        try:
            chat_id = update.effective_chat.id
        except Exception:
            print("Couldn't handle update", update)
            return
        if chat_id in self.sessions_dict.keys():
            self.sessions_dict[chat_id].dispatch_update(update)
        else:
            self._new_session(chat_id).dispatch_update(update)

    @property
    def sessions(self):
        return list(map(self.sessions_dict.get, sorted(self.sessions_dict.keys())))

    def create_task(self, cr):
        self.loop.create_task(cr)

    def start(self):
        self._t.start()

    def __repr__(self):
        return f'<#{self.id}>'
