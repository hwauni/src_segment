# -*- coding: utf-8 -*-
#!/usr/bin/python3.6

import os

log_home = os.environ.get('LOG_HOME', None)

if not log_home:
    raise ValueError('You must have "LOG_HOME" variable')

print(log_home)
