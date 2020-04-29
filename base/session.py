from abstraction.session import Session


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
