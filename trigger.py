from telegram import Update

from promise import TriggerPromise


class Trigger:
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


class UpdateTrigger:
    def load_update(self, update: Update):
        raise NotImplemented


class BaseTrigger(Trigger):
    def __init__(self):
        self._actions = list()
        self._session = None
        self._activated = False

    def activate(self):
        self._session.dispatch(self)
        self._activated = True

    @property
    def session(self):
        return self._session

    def set_session(self, session):
        self._session = session

    def hook(self, action):
        self._actions.append(action)

    @property
    def any_bonded(self) -> bool:
        return bool(self._actions)

    @property
    def actions(self):
        return self._actions
