# -*- coding: utf-8 -*-
#!/usr/bin/python3

import os
import time
import logging
import multiprocessing
from multiprocessing import Process, Queue
from pandas import Series, DataFrame
import pandas as pd

end_flag = 'q'


def ms_producer1(queue):
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2001, 2002], 'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    frame = DataFrame(data)
    queue.put(frame)

def ms_producer2(queue):
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'year': [2010, 2011, 2012, 2011, 2012], 'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    frame = DataFrame(data)
    queue.put(frame)

def ms_consumer(queue):
    idx = 0
    frame = []
    while True:
        if idx is 2:
            break
        frame.append(queue.get())
        idx = idx + 1

    frame_sum = pd.concat([frame[0], frame[1]], axis=0)
    print(frame_sum)


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

    ProcessMgr99 = ProcessMgr(ms_consumer)
    ProcessMgr1 = ProcessMgr(ms_producer1)
    ProcessMgr2 = ProcessMgr(ms_producer2)

    ProcessMgr99.produce_process(queue)
    ProcessMgr1.produce_process(queue)
    ProcessMgr2.produce_process(queue)

    ProcessMgr99.start()
    ProcessMgr1.start()
    ProcessMgr2.start()

    queue.close()
    queue.join_thread()

    ProcessMgr99.stop()
    ProcessMgr1.stop()
    ProcessMgr2.stop()
