from trigger import Trigger
from typing import List
from id import Identifiable


class State(metaclass=Identifiable):
    def bind_one(self, trigger: Trigger):
        raise NotImplemented

    def bind(self, *triggers):
        for t in triggers:
            self.bind_one(t)

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


class BaseState(State):
    def __init__(self):
        self._triggers = list()

    def __add__(self, state) -> MetaState:  # -> MetaState
        MetaState(self).__add__(state)

    def bind_one(self, trigger: Trigger):
        self._triggers.append(trigger)

    @property
    def triggers(self) -> List[Trigger]:
        return self._triggers


class ActionState(BaseState):
    def __init__(self, action):
        super().__init__()
        self.action = action


class EndState(ActionState):
    pass


class StateGenerator:
    def __init__(self, action):
        self.action = action
        self._states = {'END': EndState(action)}

    def __getitem__(self, item):
        if item in self._states.keys():
            return self._states[item]
        else:
            s = ActionState(self.action)
