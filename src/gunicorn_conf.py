import os

bind = '0.0.0.0:{}'.format(os.environ['PORT'])
loglevel = 'debug'
errorlog = '-'
accesslog = '-'
timeout = 0
workers = int(os.environ['WORKERS'])
reload = True
