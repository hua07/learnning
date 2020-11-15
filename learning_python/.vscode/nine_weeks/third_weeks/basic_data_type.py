# round（x,d）四舍五入函数对浮点数进行运算比较格式是：x是浮点数或者浮点数运算，d是保留
#的小数点的位数
#例一：
""" a = 0.1 + 0.2
if a == 0.3:
    print('正确')
else:
    print('错误')  """ #因为浮点数的运算存在不确定尾数所以输出的是错误

""" 例二：
a = round(0.1 + 0.2,1)
if a == 0.3:
    print('正确')
else:
    print('错误') """

#天天向上的力量
""" day_up = 1.0
day_factor = 0.01
for i in range(365):
    if i%7 in [6,0]:
        day_up = day_up*(1 - day_factor)
    else:
        day_up = day_up*(1 + day_factor)
print(day_up)
 """