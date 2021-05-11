"""
字面量打印与格式化
字面量类型：数值型，字符型，布尔型等

字面量插值方法：
1 格式化输出
2 通过string.format()方法拼接,支持字符串，列表，字典
    print("we are the {} and {}".format('Tom','Jerry')) 字符串
    print("we are the {0} and {1}".format(*listdata)) 列表
    print("my name is {name},my age is {age}".format(**dictdata)) 字典
3 F string 方法，也就是字符串格式化机制（>=python3.6）
"""

#第一种：格式化输出
# name = 'hogwarts'
# age = 18
# print("my name is %s"%name)
# print("my age is %d"%age)

#第二种：string.format()
name = 'hogwarts'
age = 18
listdata = ['tom','lili']
dictdata = {"name":"Tom","age":20}
print("my name is {}，my age is {}".format(name,age))
print("we are the {1} and {0}".format(*listdata)) 
print("my name is {name},my age is {age}".format(**dictdata))


#第三种：F string方法
# name = 'hogwarts'
# age = 18
# print(f"my name is {name},my age is {age}")


