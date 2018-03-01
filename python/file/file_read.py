# -*- coding: utf-8 -*-
#!/usr/bin/python3.6

logfile = "MOS_CLI_SIM.2018-02-06_16:16:04"

with open(logfile) as f:
    tmp = f.readlines()
    print(len(tmp))
    test = tmp[:10]
    print(len(test))
    test1 = tmp[10:37]
    print(len(test1))
