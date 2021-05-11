"""
字面量打印与格式化
字面量类型：数值型，字符型，布尔型等

字面量插值方法：
1 格式化输出
2 通过string.format()方法拼接,支持字符串，列表，字典
    print("we are the {} and {}".format('Tom','Jerry')) 字符串
    print("we are the {0} and {1}".format(*listdata)) 列表
    print("my name is {name},my age is {age}".format(**dictdata)) 字典
3 F-strings 方法，也就是字符串格式化机制（>=python3.6）注意{}里面可以是表达式或者函数，大括号里面不能转义，不能使用'\'
"""

#第一种：格式化输出
# name = 'hogwarts'
# age = 18
# print("my name is %s"%name)
# print("my age is %d"%age)

#第二种：string.format()
# name = 'hogwarts'
# age = 18
# listdata = ['tom','lili']
# dictdata = {"name":"Tom","age":20}
# print("my name is {}，my age is {}".format(name,age))
# print("we are the {1} and {0}".format(*listdata)) 
# print("my name is {name},my age is {age}".format(**dictdata))


#第三种：F string方法
# name = 'hogwarts'
# age = 18
# print(f"my name is {name},my age is {age}")
# print(f"result is {(lambda x: x+1)(2)}") #因为:是不允许使用，使用()可以使用



#文件的读取
# f = open('test.txt')
# print(f.readlines()) #读出来是一个列表的形式
# f.close()

#with 语句块， 可以将文件打开后，操作完毕，自动关闭文件
with open('test.txt') as f:
    print(f.readlines())




