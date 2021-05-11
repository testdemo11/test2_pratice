# -*- coding:utf-8 -*-
__author__ = 'Tnew'


import os,time

# os.mkdir("testdir")
# print(os.listdir("./"))
# # os.rmdir("testdir")
# print(os.getcwd())

#创建b文件夹
# print(os.path.exists('b'))
#
# if not os.path.exists("b"):
#     os.mkdir("b")
# if not os.path.exists("b/test.txt"):
#     f = open("b/test.txt",'w')
#     f.write("hello python")
#     f.close()

# print(time.asctime())
# print(time.localtime())
# print(time.time())
# print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())) #2021/01/20 19:12:55



#打印两天前的时间
now_timestamp=time.time()
two_day_before = now_timestamp-60*60*24*2
time_turple = time.localtime(two_day_before)
print(time.strftime("%Y/%m/%d %H:%M:%S", time_turple))

#打印3天后的时间
now_timestamp=time.time()
three_day_later = now_timestamp+60*60*24*3
time_turple = time.localtime(three_day_later)
print(time.strftime("%Y/%m/%d %H:%M:%S", time_turple))