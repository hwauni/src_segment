# -*- coding: utf-8 -*-
#!/usr/bin/python3

import os
from multiprocessing import Pool


def ms_output(number):
    idx = 0
    proc_id = os.getpid()
    print(proc_id)
    print(number)


if __name__ == "__main__":
    pool = Pool(processes=2)
    result = pool.apply_async(ms_output, (25,))
    print(result.get(timeout=1))
