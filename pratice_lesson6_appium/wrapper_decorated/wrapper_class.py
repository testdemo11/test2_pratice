# -*- coding:utf-8 -*-
__author__ = 'Tnew'


from functools import wraps

class logit:
    def __init__(self,logfile ='out.log'):
        self.logfile = logfile

    def __call__(self,func):
        @wraps(func)
        def wrapped_decorator(*args,**kwargs):
            log_string = func.__name__ + ' was called'
            print(log_string)
            with open(self.logfile,'a') as opened_file:
                opened_file.write(log_string+'\n')
            self.notify()
            return func(*args,**kwargs)
        return wrapped_decorator

    def notify(self):
        print('success')

@logit()
def myfunc1():
    pass