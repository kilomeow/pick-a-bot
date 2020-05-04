from abstraction import Action, Trigger
from meta import Identifiable


class BaseAction(Action, metaclass=Identifiable):
    def bind(self, trigger: Trigger):
        trigger.hook(self)
