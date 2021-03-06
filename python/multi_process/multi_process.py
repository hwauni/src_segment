# -*- coding: utf-8 -*-
#!/usr/bin/python3

import os
from multiprocessing import Process, Lock, current_process


def ms_output(*args):
    idx = 0
    process_id = os.getpid()

    for value in args:
        print('{0} output to {1} by process id: {2}'.format(idx, value, process_id))
        idx = idx + 1


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
    ProcessMgr = ProcessMgr(ms_output)
    ProcessMgr.produce_process(1, "test1")
    ProcessMgr.produce_process(3, "test2")
    ProcessMgr.start()
    ProcessMgr.stop()
