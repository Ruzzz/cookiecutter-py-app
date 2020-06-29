import signal
from typing import Awaitable


class OnTerminate(SystemExit):
    code = 1


def __on_terminate():
    raise OnTerminate()


def init_on_terminate(loop):
    try:
        loop.add_signal_handler(signal.SIGINT, __on_terminate)
        loop.add_signal_handler(signal.SIGTERM, __on_terminate)
    except NotImplementedError:
        pass


class AsyncCallees:

    def __init__(self):
        self.callees = list()

    def append(self, callee: Awaitable):
        self.callees.append(callee)

    async def run(self):
        for callee in self.callees:
            await callee()


on_startups = AsyncCallees()
on_shutdowns = AsyncCallees()
