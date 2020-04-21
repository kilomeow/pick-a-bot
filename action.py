from typing import List

from trigger import Trigger


class Action:
    def run(self):
        raise NotImplemented

    def bind(self, trigger: Trigger):
        raise NotImplemented

    @property
    def on_complete(self) -> Trigger:
        raise NotImplemented

    @property
    def after_triggers(self) -> List[Trigger]:
        raise NotImplemented


class BaseAction:
    def bind(self, trigger: Trigger):
        trigger.hook(self)