# -*- coding:utf-8 -*-
__author__ = 'Tnew'
"""
1 return语句用于退出函数，
向调用方返回一个表达式。执行到return语句时，会退出函数，return之后的语句不再执行 
def my_print(x):
    if x == 1:
        return False
    print('i am xiaotao')
    return True


a = my_print(1)   # 满足if，执行return False，不再执行之后的语句，跳出函数。
print(a)

# 输出：False
————————————————

2 将return语句放在try语句块中，return之后的语句还要执行
def fun():
    print(98)
    return 'ok'  # 执行到该return语句时，函数终止，后边的语句不再执行
    print(98)


def func():
    try:
        print(98)
        return 'ok'  # 函数得到了一个返回值
    finally:  # finally语句块中的语句依然会执行
        print(98)


print(fun())
print('----------')
print(func())

# 输出：
98
ok
----------
98
98
ok
————————————————

3 return在不带参数的情况下（或者没有写return语句），默认返回None。

"""
from functools import wraps
def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print('begin')
        a_func()
        print('end')
    return wrapTheFunction
@ a_new_decorator
def a_function_requiring_decoration():
    print("i am the function which need some decoraion to remove my foul smell")

a_function_requiring_decoration()
print(a_function_requiring_decoration.__name__)


def decorator_name(f):
    #@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。
    # 这可以让我们在装饰器里面访问在装饰之前的函数的属性。
    @wraps(f)
    def decorated(*args,**kwargs):
        if not can_run:
            return 'not run'
        return f(*args,**kwargs)
    return decorated

@decorator_name
def func():
    return('function is running')

# can_run = True
# print(func())
can_run = False
print(func())