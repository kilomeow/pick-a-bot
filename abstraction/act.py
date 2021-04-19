from __future__ import annotations
from typing import List, Sequence, Union

from meta.id import Identifiable

import abstraction.promise as promise
import abstraction.result as result


class Action(metaclass=Identifiable):
    promise: promise.GenAction
    context: ContextGen
    result: result.ActionResult

    def adhere(self, trigger: Trigger):
        trigger.hook(self)

    __le__ = adhere

    @property
    def end(self) -> Context:
        return self.context.End


class Trigger(metaclass=type):
    promise: promise.GenTrigger
    actions: List[Action]

    def hook_one(self, action: Action):
        raise NotImplemented

    def hook(self, *actions: Action):
        for a in actions:
            self.hook(a)

    __call__ = hook

    def __ge__(self, actions: Union[Action, Sequence[Action]]):
        if isinstance(actions, Action):
            self.hook_one(actions)
        else:
            self.hook(*actions)

    def __le__(self, context: Context):
        context.bind(self)


class Context(metaclass=type):
    triggers: List[Trigger]

    def bind_one(self, trigger: Trigger):
        raise NotImplemented

    def bind(self, *triggers: Trigger):
        for t in triggers:
            self.bind_one(t)

    def __ge__(self, triggers: Union[Trigger, Sequence[Trigger]]):
        if isinstance(triggers, Trigger):
            return self.bind_one(triggers)
        else:
            return self.bind(*triggers)

    def __add__(self, state) -> Context:
        raise NotImplemented


class ContextGen:
    def __getattr__(self, item: str):
        raise NotImplemented
