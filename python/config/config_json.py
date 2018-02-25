# main_with_json.py
import json

with open('config.json', 'r') as f:
    config = json.load(f)

tla_log_dir = config['DEFAULT']['TLA_LOG_DIR']
print(tla_log_dir)
tf_log_dir = config['DEFAULT']['TF_LOG_DIR']
print(tf_log_dir)
