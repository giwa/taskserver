import multiprocessing

# Server Socket
bind = '127.0.0.1:8000'
backlog = 2048

# Worker Processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000
max_requests = 0
timeout = 30
keepalive = 2
debug = False
spew = False

# Logging
logfile = '/home/ken/apps/log/gunicorn/task_server_gunicon.log'
loglevel = 'info'
logconfig = None

# Process Name
proc_name = 'task_server_gunicorn'
