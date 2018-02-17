# -*- coding: utf-8 -*-
#!/usr/bin/python3

import os
import time
import logging
import multiprocessing
from multiprocessing import Process, Queue

end_flag = 'q'


def ms_producer(queue, *args):
    for item in args:
        queue.put(item)


def ms_consumer(queue):
    while True:
        item = queue.get()
        print('{} recevied from sender'.format(item))

        if item is end_flag:
            break


class ProcessMgr:
    def __init__(self, worker):
        self.process_list = []
        if not worker:
            return False
        self.worker = worker

    def produce_process(self, *args):
        process = Process(target=self.worker, args=(args))
        self.process_list.append(process)

    def start(self):
        for pro in self.process_list:
            pro.start()

    def stop(self):
        for pro in self.process_list:
            pro.join()


if __name__ == "__main__":
    queue = Queue()

    ProcessMgr1 = ProcessMgr(ms_producer)
    ProcessMgr2 = ProcessMgr(ms_consumer)

    ProcessMgr2.produce_process(queue)
    ProcessMgr1.produce_process(queue, "test1")

    time.sleep(1)
    ProcessMgr1.produce_process(queue, "q")

    ProcessMgr1.start()
    ProcessMgr2.start()

    queue.close()
    queue.join_thread()

    ProcessMgr1.stop()
    ProcessMgr2.stop()
