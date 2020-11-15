#TempConvert.py
""" TempStr = input('请输入带有符号的温度值：')
if TempStr[-1] in  ['F','f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print('转换后的温度是{:.2f}C'.format(C))
elif  TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print('转换后的温度是{:.2f}F'.format(F))
else:
    print('格式输入错误') """
#hello world的条件输出
""" num = input('请输入一个整数：')
world = 'Hello World'
if eval(num) == 0:
    print(world)
elif eval(num) > 0:
    print(world[0:2],world[2:4],world[4:6] )
else:
    print(world[0]) """
#数值运算
""" vaule = input()
sum = eval(vaule)
print('{:.2f}'.format(sum)) """
#练习题：数字转换，让用户输入一串数字，输出对应的中文数字 0-9对应零到九
""" chistr = ['零一二三四五六七八九']
intstr = input('')
for i in intstr:
    print(chistr[eval(i)],end = '')
"""
#温度转换二：温度符号放在数字前面，保留两位小数点
""" TempStr = input('请输入带有符号的温度值：')
if TempStr[0] in  ['F','f']:
    C = (eval(TempStr[1:]) - 32)/1.8
    print('转换后的温度是C{:.2f}'.format(C))
elif  TempStr[0] in ['C','c']:
    F = 1.8*eval(TempStr[1:]) + 32
    print('转换后的温度是F{:.2f}'.format(F))
else:
    print('格式输入错误')
 """
 #汇率转换：人民币与美元固定汇率 1美元 = 6.78人民币
""" money = input('请输入带有货币符号的金额：')
a = money[0:3]
if a in ['RMB','rmb']:
    usd = eval(money[3:])/6.78
    print('转换成美元是USD{:.2f}'.format(usd))
elif a in ['USD','usd']:
    rmb = eval(money[3:])*6.78
    print('转换成人民币是RMB{:.2f}'.format(rmb))
else:
    print('输入错误') """

#数字形式转换
""" chistr = '零一二三四五六七八九'
numstr = input()
for i in numstr:
    b = eval(i)
    print(chistr[b],end = '') """

