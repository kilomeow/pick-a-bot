from abstraction import Session
from meta import HashIdentifiable

from threading import Lock


class BaseSession(Session, metaclass=HashIdentifiable):
    def __init__(self, worker, bot):
        self.contexts = list()
        self.contexts_lock = Lock()
        self.bot = bot
        self.worker = worker
        self.dispatch_contexts(worker.global_entry)
        self.action_promises = list()
        self.awaiting_triggers = dict()
        print('created Session!', self.__name__)

    def dispatch_action(self, action_promise):
        # todo dispatch all contexts
        self.dispatch_contexts(action_promise.context.End)

    def dispatch_contexts(self, *contexts):
        for context in contexts:
            if context.id not in self.awaiting_triggers.keys():
                self.awaiting_triggers[context.id] = list()
            context_promises = self.awaiting_triggers[context.id]
            for t in context.triggers:
                context_promises.append(t.promise(self, context))
        self.contexts.extend(contexts)

    def dispatch_trigger(self, trigger_promise):
        ignore_trigger = False
        self.contexts_lock.acquire()
        if trigger_promise.context in self.contexts:
            self._remove_context(trigger_promise.context)
        else:
            # todo warn
            print(f"Trigger {trigger_promise.trigger} dispatched from context {trigger_promise.context}, "
                  f"but context is already removed")
            ignore_trigger = True
        self.contexts_lock.release()
        if ignore_trigger: return
        for a in trigger_promise.trigger.actions:
            self.action_promises.append(a.promise(self))

    def remove_context(self, context):
        self.contexts_lock.acquire()
        self._remove_context(context)
        self.contexts_lock.release()

    def _remove_context(self, context):
        self.contexts.remove(context)
        del self.awaiting_triggers[context.id]

    def __repr__(self):
        return f'<#self.id>'


class TelegramSession(BaseSession):
    def dispatch_update(self, update):
        self.contexts_lock.acquire()
        for context in self.contexts:
            self._apply_update(update, *self.awaiting_triggers[context.id])
        self.contexts_lock.release()

    def _apply_update(self, update, *triggers):
        ...
