from abstraction import Promise

from meta import HashIdentifiable

from toolz import partial


class CallbackActionPromise(Promise, metaclass=HashIdentifiable):
    def __init__(self, action, session, task):
        self.action = action
        self.session = session
        self.task = task


class BaseActionPromiseGen:
    def __init__(self, action, cr):
        self.action = action
        self.cr = cr

    def __call__(self, session):
        task = session.worker.create_task(self.cr(session))
        p = CallbackActionPromise(self.action, session, task)
        task.add_done_callback(partial(session.dispatch_action, p))
        return p
