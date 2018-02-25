# -*- coding: utf-8 -*-
#!/usr/bin/python3.6

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

tla_log_dir = config['DEFAULT']['TLA_LOG_DIR'] 
print(tla_log_dir)
tf_log_dir = config['DEFAULT']['TF_LOG_DIR'] 
print(tf_log_dir)
