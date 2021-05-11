# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from functools import wraps


def logit(logfile = 'out.log'):
    def black_wrapper(fun):
        #wraps为了让fun输出本身的名字
        @wraps(fun)
        def run(*args, **kwargs):
            log_string = '开始找元素'
            print(log_string)
            with open(logfile,'a',encoding='utf-8') as find_log:
                find_log.write(log_string+'\n')
            basepage = args[0]
            try:
                return fun(*args,**kwargs)
            except Exception as e:
                black_string = '在黑名单查找元素'
                with open(logfile, 'a', encoding='utf-8') as find_log:
                    find_log.write(black_string + '\n')
                for black in basepage._black_list:
                    eles = basepage.finds(*black)
                    if len(eles) > 0:
                        eles[0].click()
                        return_string = '弹框处理结束，返回查找元素'
                        with open(logfile, 'a', encoding='utf-8') as find_log:
                            find_log.write(return_string + '\n')
                        return fun(*args,**kwargs)
                raise e
            finally:
                end_string = '元素查找结束'
                with open(logfile, 'a',encoding='utf-8') as find_log:
                    find_log.write(end_string + '\n')
        return run
    return black_wrapper