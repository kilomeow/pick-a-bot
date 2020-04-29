from typing import List

from .trigger import Trigger
from .promise import ActionPromise

from meta.id import Identifiable


class Action(metaclass=Identifiable):
    @property
    def promise(self) -> ActionPromise:
        raise NotImplemented

    def stick(self, trigger: Trigger):
        raise NotImplemented

    __le__ = stick

    @property
    def on_complete(self) -> Trigger:
        raise NotImplemented

    @property
    def triggers(self) -> List[Trigger]:
        raise NotImplemented


class BaseAction:
    def bind(self, trigger: Trigger):
        trigger.hook(self)
