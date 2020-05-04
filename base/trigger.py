from abstraction import Trigger
from meta import Identifiable


class BaseTrigger(Trigger, metaclass=Identifiable):
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