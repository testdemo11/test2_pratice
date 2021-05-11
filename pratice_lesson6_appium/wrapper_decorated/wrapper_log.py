# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from functools import wraps


# def logit(func):
#     @wraps(func)
#     def with_logging(*args,**kwargs):
#         print(func.__name__+' was called')
#         return func(*args,**kwargs)
#     return with_logging
#
# @logit
# def additon_func(x):
#     return x+x
#
#
# additon_func(2)


def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_decorator(*args,**kwargs):
            log_string = func.__name__ + ' was called'
            print(log_string)
            with open(logfile,'a') as opened_file:
                opened_file.write(log_string + '\n')
            return func(*args,**kwargs)
        return wrapped_decorator
    return logging_decorator

@logit()
def myfunc():
    pass

myfunc()

@logit(logfile='out2.log')
def myfunc2():
    pass

myfunc2()