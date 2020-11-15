
# -*- coding: utf-8 -*-
# while 简单练习
'''count = 1
while count <= 10:
    
    print(count)
    count += 1
    '''
# while第二个练习题
'''
count = 1
while count < 10:
    if count % 2 == 0:
        print(count)
    count += 1
print('end')
'''
# 猜年龄游戏版
'''
count = 1
while count <= 3:
    age = int(input('请输入猜测年龄：'))
    time = 3 - count
    if age == 18:
        print('真聪明，猜对了')
        break
    else:
        print('猜测错误，你还有%s机会'%time)
        count += 1
        if time == 0:
            ask = input('机会已用完，是否继续（Y/N）')
            if ask == 'Y':
                count = 1
                continue
            else:
                break
print('end')
'''
# 移动客服的提示框
"""

print('''欢迎致电10086
1、智能语音
2、人工服务
3、编码查询
''')
num = int(input('请输入你选择的业务编号：'))
if num == 1:
    print('智能语音')
elif num == 2:
    print('''1、话费查询
     2、业务办理
     3、流量查询

    ''')
elif num == 3:
    print('编码查询')
else:
    print('输入错误，再见')
"""


#游戏登录界面

""" count = 1

while count <= 3:
    time = 3 - count
    user_name = input('请输入你的昵称：')
    passward = input('请输入你的密码：')
    if user_name == 'alax' and passward == '666':
        print('欢迎登录')
        break
    else:
        print('账号或密码错误，请重新输入，还有%s机会'%time)
        if time == 0:
            print('今日机会已用完，请明天再试')
            break
    count += 1  """




