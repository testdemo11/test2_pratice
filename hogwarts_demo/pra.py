"""
猜数字游戏
计算机给一个1到100之间的随机数猜
计算机根据人猜的数字分别给出提示大一点、小一点、猜对了
"""

import random

comp_num = random.randint(1,100)

while True:
    p_num = int(input("输入一个数字： "))
    if p_num<comp_num:
        print("大一点")
    elif p_num>comp_num:
        print("小一点")
    else:
        print("猜对了")
        break