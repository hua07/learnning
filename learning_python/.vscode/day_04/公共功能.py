""" name = 'alaxlsdfasd'
v1 = name[0:8:4]
print(v1) """
# for循环
""" name = 'alax'
for lexm in name:
    print(lexm)
print(lexm) """
#练习题：请打印 1-10
""" name = range(1,11)
for num in name:
    print(num) 
print('结束')  """
# 练习题：请打印 1-10不打印 7
""" name = range(1,11)
for num in name:
    if num != 7:
        print(num) """
# for和while，有穷尽的优先用for，无穷尽优先用while
""" count = range(3)
for i in count:
    num = int(input('请输入你猜测的数字：'))
    if num == 8:
        print('你真聪明，猜对了')
        break
    elif num < 8:
        print('猜错了，有点小了')
    else:
        print('猜错了，有点大了')
print('game over')  """
print('hello','word',sep=',',end='!')
print('hello,word',end='! \n')
     






