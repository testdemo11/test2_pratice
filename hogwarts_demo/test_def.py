"""
默认参数
默认参数在定义函数的时候使用k=v的形式定义
调用函数时，如果没有传递参数，则会使用参数
如果传递参数的话，则会使用传递的参数
"""

# def func(a=2):
#     print("参数a的值为",a)

# func(4)


"""
关键字参数
在调用函数的时候，使用k=v的方式进行传参
在函数调用/定义中，关键字参数必须跟在位置参数的后面
"""

# def func(a,b,c,d):
#     print("参数a的值为",a)
#     print("参数b的值为",b)
#     print("参数c的值为",c)
#     print("参数d的值为",d)

# # func(2,d=5,c=2,b=3)
# # func(2,5,d=2,c=3)
# func(2,5,2,d=3)

"""
特殊参数
仅限关键字参数，
在[仅限关键字]形参前放置一个*
"""

# def func(a,b,c,*,d):
#     print("参数a的值为",a)
#     print("参数b的值为",b)
#     print("参数c的值为",c)
#     print("参数d的值为",d)

# func(2,5,2,d=3)  #正常输出
# func(2,1,3,1) #func() takes 3 positional arguments but 4 were given


"""
Lambda 表达式
"""
# func = lambda x:x+2
# print(func(2))

func = lambda x,y:x+y
print(func(2,4))

"与上面的lambda表达式效果一样"
# def fun2(x):
#     return x+2
# print(fun2(3))