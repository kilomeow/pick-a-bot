from threading import Lock
from toolz import partial


class Identifiable:
    def __new__(cls, class_name, parents, attributes):
        print(class_name, 'created')
        t = type(class_name, parents, attributes)
        t.__last_ID = 0
        t.__ID_lock = Lock()
        t.set_id = partial(cls.set_id, t)
        t.__new__ = cls.new_instance
        return t

    @staticmethod
    def set_id(self, instance):
        self.__ID_lock.acquire()
        self.__last_ID += 1
        instance.id = self.__last_ID
        self.__ID_lock.release()

    @staticmethod
    def new_instance(self, *args, **kwargs):
        instance = object.__new__(self)
        self.set_id(instance)
        return instance
