def auth(f):
    def inner(*args, **kwargs):
        login()
        if status['statu'] == False:
            ret = f(*args, **kwargs)
            return ret

    return inner


status = {
    'king': '123',
    'statu':True,
}


def login():
    while status['statu']:
        username = input('请输入你的账号：').strip()
        password = input('请输入你的密码：').strip()
        if username in status and status[username] == password:
            print('登录成功')
            status['statu'] = False
            return 
        elif username not in status:
            print('无此用户，请先注册账号')
        else:
            print('账号或密码错误，请重新输入')
            continue


def register():
    username = input('请输入你的账号：').strip()
    password = input('请输入你的密码:')
    status[username] = password


@auth
def article():
    print('欢迎访问文章页面')


@auth
def comment():
    print('欢迎访问评论页面')


@auth
def dariy():
    print('欢迎访问日记页面')


article()
comment()
dariy()
