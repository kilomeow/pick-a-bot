from __future__ import annotations
from typing import Callable, TypeVar, Generic

T = TypeVar('T')
U = TypeVar('U')


class AwaitableMonadTypeClass(Generic[T], metaclass=type):
    # def __rshift__(self, func: Callable[[T], U]) -> AwaitableMonadTypeClass[U]:
    #     raise NotImplemented

    def __rshift__(self, func):
        raise NotImplemented