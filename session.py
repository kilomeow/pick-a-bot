from typing import List

from action import Action, Trigger


class Session:
    def __init__(self):
        raise NotImplemented

    def dispatch(self, trigger):
        raise NotImplemented

    @property
    def current_triggers(self) -> List[Trigger]:
        raise NotImplemented

    def apply(self, action: Action):
        raise NotImplemented


class BaseSession(Session):
    def dispatch(self, trigger):
        if not trigger.activated:
            raise RuntimeError("{0} was dispatched to {1} "
                               "before it was activated".format(trigger,
                                                                self))
        self._dispatch_actions(trigger.actions)
        trigger.set_dispatched()

    def _dispatch_actions(self, actions):
        raise NotImplemented
