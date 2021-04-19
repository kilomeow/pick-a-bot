from abstraction import Action, Trigger
from meta import Identifiable

import base.context
import base.promise


class BaseAction(Action, metaclass=Identifiable):
    def __init__(self):
        self.context = base.context.ActionContextGen(self)
