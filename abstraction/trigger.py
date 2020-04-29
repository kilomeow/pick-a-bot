from telegram import Update

from .promise import TriggerPromise

from meta.id import Identifiable


class Trigger(metaclass=Identifiable):
    @property
    def promise(self) -> TriggerPromise:
        raise NotImplemented

    def hook(self, action):  # action: Action
        raise NotImplemented

    def __call__(self, *args, **kwargs):
        for a in args:
            self.hook(a)

    __ge__ = hook

    def __le__(self, state):
        state.bind(self)

    @property
    def any_hooked(self) -> bool:
        raise NotImplemented

    @property
    def actions(self):  # -> List[Action]
        raise NotImplemented


class UpdateTrigger(Trigger):
    def load_update(self, update: Update):
        raise NotImplemented
