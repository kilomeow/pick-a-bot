from threading import Lock

# Lock in the future must be replaced with mechanism which allows to create
# non-conflicting ids for all application instances


class Identifiable(type):
    def __new__(mcs, class_name, parents, attributes):
        c = type.__new__(mcs, class_name, parents, attributes)
        return c

    def __init__(cls, class_name, parents, attributes):
        super().__init__(class_name, parents, attributes)
        cls.__last_ID = 0
        cls.__ID_lock = Lock()
        cls.__new__ = cls.new_instance
        cls.id = property(cls.full_id)

    def set_id(cls, instance):
        cls.__ID_lock.acquire()
        cls.__last_ID += 1
        instance._id = cls.__last_ID
        cls.__ID_lock.release()

    def new_instance(cls, *args, **kwargs):
        instance = object.__new__(cls)
        cls.set_id(instance)
        return instance

    def full_id(cls, instance):
        return f"{cls.__name__}:{instance._id}"
