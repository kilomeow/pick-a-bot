from __future__ import annotations
from typing import List
from telegram import Bot

import abstraction.act as act


class Worker:
    sessions: List[Session]

    def create_task(self, cr):
        raise NotImplemented

    def run(self):
        raise NotImplemented


class Session(metaclass=type):
    bot: Bot
    entry: act.Context
    contexts: List[act.Context]
    worker: Worker
