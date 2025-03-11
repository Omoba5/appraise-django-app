import multiprocessing

# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "Appraise.wsgi:application"

# The socket to bind
bind = "127.0.0.1:8000"

# The number of worker processes for handling requests
workers = multiprocessing.cpu_count() * 2 + 1
timeout=30

# Disable code reload
reload = False

# The granularity of Error log outputs
loglevel = "info"
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
capture_output = True