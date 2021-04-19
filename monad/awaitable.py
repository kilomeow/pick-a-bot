from abstraction import AwaitableMonadTypeClass, Generic, T

def curry1(func, kwarg=None):
    if kwarg is not None: ...
    def curried_head(*arg1, **kwarg1):
        if kwarg1:
            if len(kwarg1.keys()) == 1:
                ...
            else:
                raise TypeError("there could be only one keyword arguments")
        def curried_tail(*args, **kwargs):
            func(arg1, *args, **kwargs)
        return curried_tail
    return curried_head

import adt

# @adt
# class:
#    Case
#


class AwaitableMonadicType(type):
    @classmethod
    def new_type(mcs, class_name, parents, attributes):
        return type.__new__(mcs, class_name, parents, attributes)
        # todo parents+(Generic[T],)

    def __new__(mcs, class_name, parents, attributes, target=type(None)):
        t = mcs.new_type(class_name, parents, attributes)
        t.__original_name = class_name
        t.__original_parents = parents
        t.__original_attributes = attributes
        return t

    def __init__(cls, class_name, parents, attributes, target=type(None)):
        super().__init__(class_name, parents, attributes)
        cls._instantiate_target(target)

    def _instantiate_target(cls, target):
        ...
        cls.target = target

    def __getitem__(cls, type_obj):
        if not isinstance(type_obj, type):
            raise TypeError("target type must be instance of `type`")
        name = f'{cls.__original_name}[{type_obj.__name__}]'
        t = cls.new_type(name, cls.__original_parents, cls.__original_attributes)
        t.__init__(name, cls.__original_parents, cls.__original_attributes)
        return t

    def __repr__(cls):
        return f'<{type(cls).__name__} : {cls.__name__}>'


class AwaitableMonad(AwaitableMonadTypeClass, metaclass=AwaitableMonadicType):
    def __rshift__(self, func):
        if len(func.__code__.co_varnames) > 1:
            ...


class PrimitiveAwaitable:

    async def result(self):
        raise NotImplemented

    __await__ = result