try:
    from queue import Queue as queue
except ImportError:
    from queue import queue as queue

from queue import Full

import traceback
from graypy import GELFHandler
from threading import Thread


class AsyncGELFHandler(GELFHandler, Thread):
    def __init__(self, *args, **kwargs):
        max_queue_size = kwargs.pop('max_queue_size', 10000)
        super(AsyncGELFHandler, self).__init__(*args, **kwargs)
        Thread.__init__(self)
        self.output_queue = queue(maxsize=max_queue_size)

        # Start thread
        self.start()

    def send(self, s):
        try:
            self.output_queue.put(s, block=False)
        except Full:
            # cannot log here, our queue is full.. just drop the message
            pass

    def _process_queue_record(self, s):
        super(GELFHandler, self).send(s)

    def run(self):

        while True:
            try:
                record = self.output_queue.get()
                self._process_queue_record(record)
                self.output_queue.task_done()
            except Exception as ex:
                # Handle log sending exception in some way. eg. traceback.print_exc():
                # Exception handling is mandatory, otherwise the thread will die
                traceback.print_exc()
