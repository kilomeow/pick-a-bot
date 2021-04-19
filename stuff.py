from typing import List

from abstraction import Action, Trigger, Session
from base import BaseAction, BaseTrigger


class EntryTrigger(BaseTrigger):
    def set_session(self, session):
        ...


class OnCompleteTrigger(BaseTrigger):
    def __init__(self, ac):
        ...


class ReplyText(BaseAction):
    def __init__(self, text=None):
        self.text = text


class ChatSession(Session):
    def __init__(self, chat_id=None):
        self.chat_id = chat_id
        self._current_triggers = []

    @property
    def current_triggers(self) -> List[Trigger]:
        ...

    def apply(self, action : Action):
        ...


async def f():
    return 3


async def h():
    x = await f()
    return x
