def func():#账号的注册
    username = input('请输入用户名：')
    password = input('请输入密码：')
    with open('账号信息',mode = 'w',encoding = 'utf-8') as f1:
        f1.write(f'{username}\n{password}')
    return '恭喜您注册成功！'
func()