# #基础的数据类型总览与简单应用
# #int bool str 之间的转换
# """ int《----》str
# int(str)字符串必须全部由数字组成
# str(int)

# int <--->bool
# 非零即True

# str<--->bool
# 非空即True """
# #int 主要用于运算，还有不同进制之间的转换
# #0001 1010转十进制，42转二进制
# """
# 0001 1010 ----> 十进制 b
# b= 0*2**1+1*2**2+0*2**3+1*2**4+1*2**5

# 42 --->  二进制 c
# c = 42对2取余，不足8位，前面补0
#  """
# #字符串的常用操作方法
# #upper lower  不会对原字符串进行任何操作，都是产生一个新的字符串。

# #做一个用户登录系统，需要用户填写验证码，但是不需要大小写
# username = input('请输入用户名：')
# password = input('请输入密码：')
# code = 'qWae'
# print(code)
# your_code = input('请输入验证码：')
# if your_code.upper() == code.upper():
#     if username == 'wang' and password == '123':
#         print('登录成功')
# else:
#     print('验证码错误')
# #startswith  endswith 验证字符串是否是以什么开头或结尾。返回True或者False
# #replace 代替，替换
# msg = 'alex很nb，alex是老男孩教育的创始人之一，alex长的很帅'
# msg1 = msg.replace('alex', '太白')
# print(msg1)

# #strip 去除空白
# s4 = '\n太白\t'
# s5 = s4.strip()
# #可以去除指定的字符
# s6 = 'rre太白qsd'
# s7 = s6.strip('qsdre')
# print(s7)
# #split 非常重要,默认按照空格分隔，返回一个列表。还可以指定分隔符
# s8 = '太白 女神 吴超'
# l = s8.split()
# print(l)

# #join  前提是列表里的元素必须都是str类型
# s1 = ['女神', '太白']
# s2 = '，'.join(s1)
# print(s2, type(s2))

# #count 计算某个元素出现的次数
# #format 格式化输出
# #第一种用法：
# msg = '我叫{}今年{}性别{}'.format('大壮', 25, '男')
# #第二种方法：
# msg = '我叫{0}今年{1}性别{2}'.format('大壮', 25, '男')
# #第三种方法：
# msg = '我叫{name}今年{age}性别{sex}'.format(
#     sex='男',
#     name='大壮',
#     age=25,
# )

# #is 系列
# """
# name = 'taibai124'
# print(name.isalnum())#字符串由字母或数字组成
# print(name.sialpha())#字符串只由字母组成
# print(name.isdicimal())#字符串字由十进制组成

# """

# #成员运算，in notin

# #for 循环
# s1 = '老男孩教育最好的讲师：太白'
# #分别使用while循环和for循环打印s1里所有的元素
# """ #使用while循环
# count = 0
# while count < len(s1):
#     word = s1[count]
#     print(word)
#     count += 1
# """
# """
# #使用for循环
# for i in s1:
#     print(i) """

# #构造代码：“倒计时3秒”，“倒计时2 秒","倒计时1秒"，“出发”
# time = 3
# while time > 0:
#     print(f'倒计时{time}秒')
#     time -= 1
# else:
#     print('出发')

# 1. 将字符串 "abcd" 转成大写
# word = 'abcd'
# # word = word.capitalize() # 这是首字母大写
# word = word.upper() #全部大写
# print(word)

# 2. 计算字符串 "cd" 在 字符串 "abcd"中出现的位置
# word = 'cd'
# s = 'abcd'
# index = s.find('cd非') # 根据元素找索引，如没有此元素，返回-1
# index = s.index('cdf') # 根据元素找索引，如没有次元素，报错
# print(index)

# 3. 字符串 "a,b,c,d" ，请用逗号分割字符串，分割后的结果是什么类型的？
# s = 'abcd'
# s1 = ','.join(s) # 加入，可以用于列表转换成字符串
# s2 = s.split(',') # 以**分隔，如不指定分隔符，默认使用空格分隔，用于把字符串转换成列表
# print(s1,type(s1))
# print(s2,type(s2))

# 4. "{name}喜欢{fruit}".format(name="李雷") 执行会出错，请修改代码让其正确执行
# print('{name}喜欢{fruit}'.format(name="李雷",fruit = '韩梅梅'))
# 5. string = "Python is good", 请将字符串里的Python替换成 python,并输出替换后的结果
# string = "Python is good"
# string = string.replace('Python', 'python')
# print(string)
# 6. 有一个字符串 string =  "python修炼第一期.html"，请写程序从这个字符串里获得.html前面的部分，
# 要用尽可能多的方式来做这个事情
# string =  "python修炼第一期.html"
# #第一种方法：根据元素找索引，然后再进行切片
# new_str = string[:(string.find('.html'))]
# print(new_str)
#第二种方法
# string =  "python修炼第一期.html"
# string = string.replace('.html','')
# print(string)

# 7. 如何获取字符串的长度？
# string =  "python修炼第一期.html"
# lens = len(string)
# print(lens)

# 8. "this is a book",请将字符串里的book替换成apple
# strs = 'this is a book'
# strs = strs.replace('book','apple')
# print(strs)
# 9. "this is a book", 请用程序判断该字符串是否以this开头
# judge = strs.startswith('this')
# print(judge)
# 10. "this is a book", 请用程序判断该字符串是否以apple结尾
# judge = strs.endswith('apple')
# print(judge)
# 11. "This IS a book"， 请将字符串里的大写字符转成小写字符
# str = "This IS a book"
# strs = str.lower()
# print(strs)
# 12. "This IS a book"， 请将字符串里的小写字符，转成大写字符
# str1 = str.upper()
# print(str1)
# 13. "this is a book\n"， 字符串的末尾有一个回车符，请将其删除
# str2 = str.strip()
# print(str2)

#不用解释器执行代码，直接说出下面代码的执行结果
# string = "Python is good"
# new_str = string[1:20] # "ython is good"
# new_str = string[20] # 报错
# new_str =string[3:-4] #'hon is '
# new_str =string[-10:-3] #'0n is g'
# new_str =string.lower() #全部变小写
# new_str =string.replace("o", "0") #'pyth0n is g00d' replace如果不添加次数默认全部替换
# new_str =string.startswith('python') # flase
# new_str =string.split() #['Python', 'is', 'good']
# new_str =len(string) # 14 len在计算长度时，空格也占用一个长度
# new_str =string[30] #报错
# new_str =string.replace(" ", '')# 'Pythonisgood'
# print(new_str)