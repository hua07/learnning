""" import turtle

turtle.pensize(4)
turtle.pencolor('red')

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.mainloop() """
#使用变量保存数据，并进行算术运算
""" a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d'%(a,b,a+b))
print('%d - %d = %d'%(a,b,a-b))
print('%d * %d = %d'%(a,b,a*b))
 """
#练习：华氏温度转摄氏温度
# F = 1.8C +32
""" f = float(input('请输入华氏温度：'))
c = (f-32)/1.8
print('%.1f华氏度= %.1f摄氏度'%(f,c)) """
#练习：输入半径计算周长和面积
""" import math
radius = float(input('请输入半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius **2
print('周长：%.2f'%perimeter)
print('面积：%.2f'%area) """
#练习：输入年份判断是不是闰年
""" year = int(input('请输入年份：'))
is_leap = (year % 4 == 0 and year != 0)
print(is_leap) """
#循环结构 for in循环和 while循环
#用for循环实现1~100的和
""" 
sum = 0
for X in range(101):
    sum += X
print(sum) """
#用for循环实现1~100之间偶数的和
""" sum = 0
for X in range(2,101,2):
    sum += X
print(sum) """
#猜数字游戏
#计算机出一个1~100之间的随机数由人来猜
#计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
""" import random
answer = random.randint(1,100)
counter = 0 
while True:
    counter += 1
    number = int(input('请输入你猜测的数字：'))
    if number < answer:
        print('有点小了，请重新输入')
    elif number > answer:
        print('有点大了，请重新输入')
    else:
        print('恭喜你答对了')
        break
print('你总共猜了%d次'%counter)
if counter > 7:
    print('你智商余额明显不足') """
#输出乘法口诀表
""" for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(j,i,i*j),end = '\t')
    print() """
#求取水仙数（自幂数的一种）
""" for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            num = x*100 +y*10+z
            if num == x**3+y**3+z**3:
                print(num)
print('共有以上四个水仙数') """
""" flast_name = 'wang'
last_name = 'jinhua'
full_name = flast_name + ' ' +last_name
print(full_name.lower()) """
#练习题：输入自己喜欢的名人名句并把名人的名字用大写或者小写打印出来。
""" name = input('请输入你喜欢的名人名称：')
Word = input('请输入你喜欢的名人名句：')
name = name.title()
print(name,':','"',Word,'"') """
""" age = 23
messge = 'happy' + str(age) + 'birthday'
print(messge) """
""" print(r''' "To be,or not to be":that is the question.
whether it's nober in the mind to suffer.''')
print(r'''静夜思
床前明月光
疑似地上霜
举头望明月
低头思故乡''') """
""" a = 'python'
print('hello,',a or 'world')

b = ''
print('hello,',b or 'world') """
#可更改的有序的列表list
""" L = ['Adam','Lisa','paul','Bart',]
L[0] = 'Bart'
L[-1] = 'Adam'
print(L) """
#不可更改的有序列表tuple
""" t = ('Adam','Lisa','Bart')
num = (0,1,2,3,4,5,6,7,8,9)
text = ('a','b',['A','B'])
new_text = ('a','b',('A','B'))
print(text)
print(new_text) """
#if 条件语句
#练习题：如果成绩在60分或以上，视为passed.
""" score = 55
if score >= 60:
    print('passed')
else:
    print('falled')
print('end') """
#练习题：90分以上：Excelllect,80以上：good,60以上：passed,60以下：falled
""" score = 85
if score >= 90:
    print('excellect')
elif score >= 80:
    print('good')
elif score >= 60:
    print('passed')
else:
    print('falled') """
#for 循环
#班级考试后，老师需要统计班里同学的平均成绩，已知4位同学的成绩用list表示如下：
""" L = [75,92,59,68,]
sum = 0.0
for i in L:
    sum += i
print(sum/4) """
#while循环不会迭代list或tuple的元素，而是根据表达式判断循环是否结束。
#利用循环打印出100以内的所有奇数的和。
""" sum = 0
x = 1
while x <= 100:
    sum += x
    x += 2
print(sum) """
#利用while ture 配合break语句，计算1~20项的和：
""" sum = 0
x = 1
while True:
    if x == 21:
        break
    sum += x
    x += 1
print(sum) """
#continue语句
#练习：通过增加continue语句，计算奇数的和：
""" sum = 0
x = 0
while True:
    x += 1
    if x > 100:
        break
        
    if x % 2 == 0:
        continue
    sum += x
print(sum) """
#python之多重循环
#练习题：对100以内的两位数，请使用两种循环打印出所有十位数数字比个位数数字小的数。

#for循环的方法
"""  x = [1,2,3,4,5,6,7,8,9]
y = [0,1,2,3,4,5,6,7,8,9]
for i in x:
    for t in y:
        if 10*i + t < 100 and i<t:
            print(10*i + t) """

#while循环的方法
""" x = 1
y = 0
while 10*x + y < 100:
    while y <= 9:
        if x < y:
            print(10*x + y)
        y += 1
    x += 1
    y = 0 """


    




