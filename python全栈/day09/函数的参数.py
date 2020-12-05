# def new_len(Iterative):  #函数的定义：接受的参数形式参数
#     count = 0
#     for i in Iterative:
#         count += 1
#     return count

# s2 = 'adfwertkjglm'
# print(new_len(s2))  #函数的执行传的参数：实际参数

#实参角度：
#位置参数必须是一一对应。

#写一个函数，只接受两个int的参数，函数的功能是将较大的数返回。
# def new_max(a,b):
#     c = a if int(a)>int(b) else b  #三元运算符：简单的if else
#     return int(c)
# print(new_max(200,150))

#关键字参数：如果难道函数需要参数特别多，有很多时候需要关键字参数。也必须一一对应
#函数：传入两个字符串参数，将两个参数拼接完成结果返回。
# def splicing(s1, s2):
#     word = f'姓名：{s1}\n性别：{s2}'
#     return word

# name = 'king'
# sex = 'man'
# print(splicing(name, sex))
# print(splicing(s2='女', s1='alex'))

#混合传参：既有关键子，又有位置参数。位置参数一定要在关键字参数的前面
#实参角度总结:
#   1、位置参数 按照顺序，一一对应
#   2、关键字参数，一一对应
#   3、混合参数，位置参数一定要在关键字参数前面

#写一个函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新的内容返回给调用者。
# def my_len(li):
#     count = 0
#     for i in li:
#         count += 1
#     if count > 2:
#         li = li[:2]
#     return li

# lis = ['king', 1, 4, ]
# lis1 = ['name', 2]
# print(my_len(lis))
# print(my_len(lis1))

# 默认值参数：默认参数设置的意义：普遍经常使用的。

#写一个函数完成三次登录功能，再写一个函数完成注册
# def sign_in():
#     dic = {'wang': '123', 'king': '123', 'hua': '123'}
#     ver_code = 'qwer'
#     print(ver_code)
#     while 1:
#         username = input('请输入你的账号名：')
#         password = input('请输入你的密码：')
#         code = input('请输入验证码（不区分大小写）：')
#         count = 0
#         if count < 3:
#             if code.upper() == ver_code.upper():
#                 if username in dic and password == dic[username]:
#                     print('登录成功')
#                     break
#                 else:
#                     print('账号或密码错误')
#                     count += 1
#             else:
#                 print('验证码错误')
#         else:
#             print('3次机会使用完毕，请明天再试')
#             break

# sign_in()

# def register():
#     dic = {}
#     username = input('请输入你的用户名：').strip()
#     password = input('请输入你的密码：').strip()
#     dic.setdefault(username,password)
#     s = print('注册成功')
#     return s
# register()


#对上题进行实际更改，现实中账号和密码肯定是在一个文件里
def func():  #账号的注册
    username = input('请输入用户名：')
    password = input('请输入密码：')
    with open('账号信息', mode='w', encoding='utf-8') as f1:
        f1.write(f'{username}\n{password}')
    return '恭喜您注册成功！'


func()