import random
import string


class HashIdentifiable(type):

    HASH_LENGTH = 6

    def __new__(mcs, class_name, parents, attributes):
        c = type.__new__(mcs, class_name, parents, attributes)
        return c

    def __init__(cls, class_name, parents, attributes):
        super().__init__(class_name, parents, attributes)
        cls.__new__ = cls.new_instance
        cls.id = property(cls.full_id)

    @staticmethod
    def set_hash(instance):
        instance._hash = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))

    def new_instance(cls, *args, **kwargs):
        instance = object.__new__(cls)
        cls.set_hash(instance)
        return instance

    def full_id(cls, instance):
        return f"{cls.__name__}:{instance._hash}"
