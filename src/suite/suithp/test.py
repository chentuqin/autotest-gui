#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，
超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？


i = int(input("利润："))

arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for j in range(0,6):
    if i>arr[j]:
        r += (i-arr[j])*rat[j]
        print((i-arr[j])*rat[j])
        i = arr[j]
print(r)



输入三个整数x,y,z，请把这三个数由小到大输出。

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
arr = [x,y,z]  

for i in range(0,3):
    for j in range(i,3):
        if arr[i] > arr[j]:
            k = arr[i]
            arr[i] = arr[j]
            arr[j] = k
print(arr)

题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

在数学上，费波那契数列是以递归的方法来定义：

输出 9*9 乘法口诀表


for i in range(1,10):
    print(end='\n')
    for j in range(1,1+i):
        print("%d*%d=%d"%(j,i,i*j),end=' ')




import time
timess = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
print(timess)
time.sleep(3)
timess = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
print(timess)
timess = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
print(timess)

有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子
，假如兔子都不死，问每个月的兔子总数为多少？
'''



a = 21
b = 10
c = a % b
print(c)
print("5 - c 的值为：", c)
