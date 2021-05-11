# -*- coding:utf-8 -*-
__author__ = 'Tnew'
"""
def 作为函数，放在类的外面；
def 作为方法，放在类的里面；

面向对象
类变量：在类里面声明的变量，不在方法之中，访问是通过手动调用
实例变量：self.变量名的方式访问,实例变量的作用域是整个类中的所有方法
普通变量：在类方法之中，没有self开头，作用域是本方法之中

构造方法：
给创建的对象建立标识符
为对象数据成员开辟内存空间
完成对象数据的初始化

self:
代表类的实例
"""

class Person:
    #类变量
    name = "default"
    age = 0
    gender = 'male'
    weight = 0

    #构造方法，在类实例化的时候被调用
    def __init__(self,name,age,gender,weight):
        #实例变量， self.变量名的方式访问,
        #实例变量的作用域是整个类中的所有方法
        self.name =name
        self.age =age
        self.gender=gender
        self.weight=weight

    @classmethod
    def eat(self):
        print(f" {self.name} is eating")

    def play(self):
        print("playing")

    def jump(self):
        print("jump")


#类方法与实例方法的区别
#类方法不能访问实例方法，如果需要访问，需要加个装饰器@classmethod
Person.eat() #不加classmethod不能访问
# zs = Person('zhangsan',25,'male',120)
# zs.eat()


#类变量与实例变量的区别,两个变量可以被修改
#类变量是需要类来访问的，实例变量是需要实例来访问
# print(Person.name)
# Person.name = 'tom'
# print(Person.name)
# zs = Person('zhangsan',25,'male',120)
# print(zs.name)
# zs.name = 'LILI'
# print(zs.name)




# zs = Person('zhangsan',25,'male',120)
# zs.eat()
# zs.set_param("zhangsan")
# print(zs.name)
# zs.set_age(20)
# print(zs.age)
# print(f"张三的名字是{zs.name},张三的年龄是{zs.age},性别是{zs.gender},体重是{zs.weight}")


# def eat(self):
#     food = "rice" #普通变量 -->在类方法之中，没有self开头，作用域是本方法之中
#     print(f" {self.name} is eating")

