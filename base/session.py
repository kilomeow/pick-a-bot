from abstraction import Session
from meta import HashIdentifiable


class BaseSession(Session, metaclass=HashIdentifiable):
    def dispatch(self, trigger):
        if not trigger.activated:
            raise RuntimeError("{0} was dispatched to {1} "
                               "before it was activated".format(trigger,
                                                                self))
        self._dispatch_actions(trigger.actions)
        trigger.set_dispatched()

    def _dispatch_actions(self, actions):
        raise NotImplemented
