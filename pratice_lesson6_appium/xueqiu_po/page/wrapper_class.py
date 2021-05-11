# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from functools import wraps


class WrapperBlack:
    def __init__(self,logfile='out.log'):
        self.logfile = logfile
    #该方法的功能类似于在类中重载 () 运算符，使得类实例对象可以像调用普通函数那样，以“对象名()”的形式使用。
    def __call__(self, func):
        @wraps(func)
        def run(*args, **kwargs):
            log_string = '开始找元素'
            self.open_file(log_string)
            basepage = args[0]
            try:
                return func(*args, **kwargs)
            except Exception as e:
                black_string = '在黑名单查找元素'
                self.open_file(black_string)
                for black in basepage._black_list:
                    eles = basepage.finds(*black)
                    if len(eles) > 0:
                        eles[0].click()
                        return_string = '弹框处理结束，返回查找元素'
                        self.open_file(return_string)
                        return func(*args, **kwargs)
                raise e
            finally:
                end_string = '元素查找结束'
                self.open_file(end_string)
        return run

    def open_file(self,string):
        with open(self.logfile,'a', encoding='utf-8') as find_log:
            find_log.write(string+'\n')
