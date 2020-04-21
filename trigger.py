from telegram import Update


class Trigger:
    def check(self, update: Update) -> bool:
        raise NotImplemented

    @property
    def hook(self, action):  # action: Action
        raise NotImplemented

    @property
    def any_bonded(self) -> bool:
        raise NotImplemented

    @property
    def actions(self):  # -> List[Action]
        raise NotImplemented


class BaseTrigger(Trigger):
    def __init__(self):
        self._actions = list()

    def hook(self, action):
        self._actions.append(action)

    @property
    def any_bonded(self) -> bool:
        return bool(self._actions)

    @property
    def actions(self):
        return self._actions
