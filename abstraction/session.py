from typing import List

from .action import Action, Trigger


class Session:
    def __init__(self):
        raise NotImplemented

    def dispatch(self, trigger):
        raise NotImplemented

    @property
    def current_triggers(self) -> List[Trigger]:
        raise NotImplemented

    def apply(self, action: Action):
        raise NotImplemented
