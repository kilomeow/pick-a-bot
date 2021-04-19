from __future__ import annotations

import abstraction.act as act
from .session import Session
from asyncio import Task


class Gen:
    def __call__(self, session: Session) -> Promise:
        raise NotImplemented


class Promise:
    session: Session
    task: Task
    status: PromiseStatus

    def reject(self):
        raise NotImplemented


class PromiseStatus:
    pass
    # Idle: Case
    # Rejected: Case[RejectionReason]
    # Working: Case
    # Completed: Case


class RejectionReason:
    pass


class ActionPromise(Promise):
    action: act.Action


class TriggerPromise(Promise):
    trigger: act.Trigger
    session: Session
    context: act.Context

    def activate(self):
        raise NotImplemented


class GenAction(Gen):
    action: act.Action

    def __call__(self, session: Session) -> ActionPromise:
        raise NotImplemented


class GenTrigger(Gen):
    trigger: act.Trigger

    def __call__(self, session: Session) -> TriggerPromise:
        raise NotImplemented
