from __future__ import annotations
from typing import List

from .trigger import Trigger
from .promise import ActionPromise
from .states import State, StateGen

from meta.id import Identifiable


class Action(metaclass=Identifiable):
    @property
    def promise(self) -> ActionPromise:
        raise NotImplemented

    def adhere(self, trigger: Trigger):
        raise NotImplemented

    __le__ = adhere

    @property
    def states(self) -> StateGen:
        raise NotImplemented

    @property
    def end(self) -> State:
        raise NotImplemented

    @property
    def triggers(self) -> List[Trigger]:
        raise NotImplemented
