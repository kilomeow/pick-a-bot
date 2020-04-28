class Promise:
    @property
    def session(self):  # session : Session
        return NotImplemented

    def set_session(self, session):  # session : Session
        raise NotImplemented


class ActionPromise:
    @property
    def action(self):  # -> Action
        raise NotImplemented

    def run(self):
        raise NotImplemented

    @property
    def started(self) -> bool:
        raise NotImplemented

    @property
    def complete(self) -> bool:
        raise NotImplemented

    @property
    def rejected(self) -> bool:
        raise NotImplemented


class TriggerPromise:
    def activate(self):
        raise NotImplemented

    def reject(self):
        raise NotImplemented

    @property
    def activated(self) -> bool:
        raise NotImplemented

    @property
    def rejected(self) -> bool:
        raise NotImplemented

    @property
    def on_activate(self):  # -> Trigger
        ...

    def set_dispatched(self):
        raise NotImplemented

    @property
    def dispatched(self) -> bool:
        raise NotImplemented
