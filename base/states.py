from abstraction.states import State, MetaState


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