from base import BaseAction, BaseActionPromiseGen


class Callback(BaseAction):
    def __init__(self):
        super().__init__()
        self.promise = BaseActionPromiseGen(self, None)

    def __call__(self, cb):
        self.promise.cr = cb
