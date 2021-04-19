from meta import HashIdentifiable


class ActionResult(metaclass=type):
    def __await__(self):
        raise NotImplemented
