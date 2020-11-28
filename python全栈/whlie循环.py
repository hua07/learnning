#利用while语句写出猜大小的游戏：设定一个数字，如果比66大，则显示猜测的结果大了，如果比66小，则显示猜测的结果小，否则提示正确
from typing import NamedTuple

num = 0
while num < 3:
    num += 1
    your_nember = int(input('请输入你猜测的数字：'))
    if your_nember == 66:
        print('猜测正确')
        break
    elif your_nember <= 66:
        print('猜测的数字小了')
    else:
        print('猜测的数字大了')
else:
    print('太笨了你')
#使用while循环输出1-10
a = 1
while a < 11:
    print(a)
    a += 1
#求1-100所有数字的和
a = 1
s = 0
while a < 101:
    s += a
    a += 1
print(s)
#输出1-100内所有的奇数
a = 1
s = 0
while a < 101:
    if a % 2 == 1:
        s += a
    a += 1
print(s)
#输出1-100内所有的偶数的和
a = 1
s = 0
while a < 101:
    if a % 2 == 0:
        s += a
    a += 1
print(s)
#用户有三次登录机会且每次输入错误时显示剩余尝试次数
num = 3
while num > 0:
    name = input('请输入你的用户名：')
    password = input('请输入你的密码：')
    if name == 'wang' and password == '123456':
        print('登录成功')
    else:
        num -= 1
        print(f'账号或密码错误请重新输入，你还有{num}次机会')