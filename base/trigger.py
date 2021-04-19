from abstraction import Trigger, Action
from meta import Identifiable


class BaseTrigger(Trigger, metaclass=Identifiable):
    def __init__(self):
        self.actions = list()

    def hook_one(self, action: Action):
        self.actions.append(action)

    @property
    def promise(self):
        ...
