#基础的数据类型总览与简单应用
#int bool str 之间的转换
""" int《----》str
int(str)字符串必须全部由数字组成
str(int)

int <--->bool
非零即True

str<--->bool
非空即True """
#int 主要用于运算，还有不同进制之间的转换
#0001 1010转十进制，42转二进制
""" 
0001 1010 ----> 十进制 b
b= 0*2**1+1*2**2+0*2**3+1*2**4+1*2**5

42 --->  二进制 c
c = 42对2取余，不足8位，前面补0
 """
#字符串的常用操作方法
#upper lower  不会对原字符串进行任何操作，都是产生一个新的字符串。

#做一个用户登录系统，需要用户填写验证码，但是不需要大小写
username = input('请输入用户名：')
password = input('请输入密码：')
code = 'qWae'
print(code)
your_code = input('请输入验证码：')
if your_code.upper() == code.upper():
    if username == 'wang' and password == '123':
        print('登录成功')
else:
    print('验证码错误')
#startswith  endswith 验证字符串是否是以什么开头或结尾。返回True或者False
#replace 代替，替换
msg = 'alex很nb，alex是老男孩教育的创始人之一，alex长的很帅'
msg1 = msg.replace('alex', '太白')
print(msg1)

#strip 去除空白
s4 = '\n太白\t'
s5 = s4.strip()
#可以去除指定的字符
s6 = 'rre太白qsd'
s7 = s6.strip('qsdre')
print(s7)
#split 非常重要,默认按照空格分隔，返回一个列表。还可以指定分隔符
s8 = '太白 女神 吴超'
l = s8.split()
print(l)

#join  前提是列表里的元素必须都是str类型
s1 = ['女神', '太白']
s2 = '，'.join(s1)
print(s2, type(s2))

#count 计算某个元素出现的次数
#format 格式化输出
#第一种用法：
msg = '我叫{}今年{}性别{}'.format('大壮', 25, '男')
#第二种方法：
msg = '我叫{0}今年{1}性别{2}'.format('大壮', 25, '男')
#第三种方法：
msg = '我叫{name}今年{age}性别{sex}'.format(
    sex='男',
    name='大壮',
    age=25,
)

#is 系列
""" 
name = 'taibai124'
print(name.isalnum())#字符串由字母或数字组成
print(name.sialpha())#字符串只由字母组成
print(name.isdicimal())#字符串字由十进制组成

"""

#成员运算，in notin

#for 循环
s1 = '老男孩教育最好的讲师：太白'
#分别使用while循环和for循环打印s1里所有的元素
""" #使用while循环
count = 0
while count < len(s1):
    word = s1[count]
    print(word)
    count += 1
"""
"""
#使用for循环
for i in s1:
    print(i) """

#构造代码：“倒计时3秒”，“倒计时2 秒","倒计时1秒"，“出发”
time = 3
while time > 0:
    print(f'倒计时{time}秒')
    time -= 1
else:
    print('出发')