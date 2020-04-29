from .trigger import Trigger

from typing import List
from meta.id import Identifiable


class State(metaclass=Identifiable):
    def bind_one(self, trigger: Trigger):
        raise NotImplemented

    def bind(self, *triggers):
        for t in triggers:
            self.bind_one(t)
a
    __ge__ = bind

    def __add__(self, state):
        raise NotImplemented

    @property
    def triggers(self) -> List[Trigger]:
        raise NotImplemented


class MetaState(State):
    def __init__(self, *states):
        self.states = list(states)

    def bind_one(self, trigger):
        for s in self.states:
            s.bind_one(trigger)

    def __add__(self, state):
        if isinstance(state, MetaState):
            self.states.extend(state.states)
        else:
            self.states.append(state)

    @property
    def triggers(self) -> List[Trigger]:
        s = set()
        for s in self.states:
            s.update(s.triggers)
        return list(s)
