from __future__ import annotations

from abstraction import Context, Trigger, ContextGen
from meta import Identifiable

from typing import List


class MetaContext(Context):
    def __init__(self, *contexts: Context):
        self.content = list(contexts)

    def bind_one(self, trigger: Trigger):
        for s in self.content:
            s.bind_one(trigger)

    def __add__(self, context: Context) -> MetaContext:
        mc = MetaContext(*self.content)
        if isinstance(context, MetaContext):
            mc.content.extend(context.content)
        else:
            mc.content.append(context)
        return mc

    @property
    def triggers(self) -> List[Trigger]:
        s = set()
        for c in self.content:
            s.update(c.triggers)
        return list(s)


class BaseContext(Context, metaclass=Identifiable):
    def __init__(self):
        self._triggers = list()

    def __add__(self, state) -> MetaContext:
        return MetaContext(self).__add__(state)

    def bind_one(self, trigger: Trigger):
        self._triggers.append(trigger)

    @property
    def triggers(self) -> List[Trigger]:
        return self._triggers


class ActionContext(BaseContext):
    def __init__(self, action, name=""):
        super().__init__()
        self.action = action
        self.name = name

    def __repr__(self):
        return f'<#{self.id} :: {self.name} <- #{self.action.id}>'


class ActionContextGen(ContextGen):
    def __init__(self, action):
        self.__dict__["action"] = action
        self.__dict__["_contexts"] = {'End': ActionContext(action, "End")}

    def __getattr__(self, item):
        if item in self._contexts.keys():
            return self._contexts[item]
        else:
            s = ActionContext(self.action, item)
            self.__dict__["_contexts"][item] = s
            return s

    def __setattr__(self, item, value):
        self._contexts[item] = value
