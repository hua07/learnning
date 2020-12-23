# 装饰器：在不改变原被装饰的函数的源代码以及调用方式下，为其添加额外的功能。
# 开放封闭原则;
# 开放：对代码的拓展开放的
# 封闭：对源码的修改是封闭的。
# def index():
#     print('欢迎访问博客园主页')

#需求介绍：你现在在某公司的开发部任职，领导给你一个业务需求让你完成：让你写代码测试上面函数的执行效率。
#需求分析：你想要测试此函数的执行效率，你应该怎么做？应该在此函数执行前记录一个时间，执行完毕之后记录一个时间，这个时间差
# 就是具体此函数的执行效率。那么执行时间如何获取呢？可以利用time模块，有一个time.time()功能。
# import time

# def index():
#     print('欢迎访问博客园主页')

# start_time = time.time()
# index()
# end_time = time.time()
# print(f'此函数的执行效率为{end_time-start_time}')

# # 由于index函数自由一行代码，执行效率太快了，所以我们利用time模块的一个sleep模拟一下。
# import time

# def index():
#     time.sleep(2)
#     print('欢迎访问博客园主页')

# start_time = time.time()
# index()
# end_time = time.time()
# print(f'此函数的执行效率为{end_time-start_time}')

# def my_time(iterable):
#     start_time = time.time()
#     iterable()
#     end_time = time.time()
#     return f'此函数的执行效率为{end_time-start_time}'

# time = my_time(index)
# print(time)

# def my_time(func):
#     def inner():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print(f'此函数的执行效率为{end_time-start_time}')

#     return inner

# f = my_time(index)
# f()

# 我们分析一下以上代码，代码执行到这一行：f = timer(index) 先执行谁？看见一个等号先要执行等号右边，
# timer(index) 执行timer函数将index函数名传给了func形参。内层函数inner执行么？不执行，inner函数返回 给f变量。
# 所以我们执行f() 就相当于执行inner闭包函数。 f(),这样既测试效率又执行了原函数，有没有问题？当然有啦！！
# 版本4你要解决原函数执行方式不改变的问题，怎么做？ 所以你可以把 f 换成 index变量就完美了！
# index = timer(index) index()带着同学们将这个流程在执行一遍，特别要注意 函数外面的index实际是inner函数的内存地址而不是
# index函数。让学生们抄一遍，理解一下，这个timer就是最简单版本装饰器，
# 在不改变原index函数的源码以及调用方式前提下，为其增加了额外的功能，测试执行效率。

# 你现在这个代码，完成了最初版的装饰器，但是还是不够完善，因为你被装饰的函数index可能会有返回值，如果有返回值，
# 你的装饰器也应该不影响，开放封闭原则嘛。但是你现在设置一下试试：
# import time

# def index():
#     time.sleep(2)
#     print('欢迎访问博客园主页')
#     return '访问成功'

# def timer(func):
#     def inner():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print(f'此函数的执行效率为{end_time-start_time}')

#     return inner

# index = timer(index)
# print(index())
# 加上装饰器之后，他的返回值为None，为什么？因为你现在的index不是函数名index，这index实际是inner函数名。
# 所以index() 等同于inner() 你的 '访问成功'返回值应该返回给谁？应该返回给index，这样才做到开放封闭，实际返回给了谁？
# 实际返回给了func，所以你要更改一下你的装饰器代码，让其返回给外面的index函数名。 所以：你应该这么做：
# import time

# def index():
#     time.sleep(3)
#     print('欢迎访问博客园主页')
#     return '访问成功'

# def timer(func):
#     def inner():
#         start_time = time.time()
#         ret = func()
#         end_time = time.time()
#         print(f'此函数的执行效率为{end_time-start_time}')
#         return ret

#     return inner

# index = timer(index)
# print(index())
# 到目前为止，你的被装饰函数还是没有传参呢？按照我们的开放封闭原则，加不加装饰器都不能影响你被装饰函数的使用。所以我们看一下。
# import time

# def index():
#     time.sleep(2)
#     print('欢迎访问博客园主页')
#     return '访问成功'

# def home(name):
#     time.sleep(3)
#     print(f'欢迎访问{name}主页')

# def timer(func):
#     def inner():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print(f'此函数的执行效率为{end_time-start_time}')

#     return inner

# home = timer(home)
# home('太白')
# 上面那么做，显然报错了，为什么？ 你的home这个变量是谁？是inner，home('太白')实际是inner('太白')但是你的'太白'
# 这个实参应该传给谁？ 应该传给home函数，实际传给了谁？实际传给了inner，所以我们要通过更改装饰器的代码，
# 让其将实参'太白'传给home.

# import time

# def index():
#     time.sleep(2)
#     print('欢迎访问博客园主页')
#     return '访问成功'

# def home(name):
#     time.sleep(3)
#     print(f'欢迎访问{name}主页')

# def timer(func):
#     def inner(name):
#         start_time = time.time()
#         func(name)
#         end_time = time.time()
#         print(f'此函数的执行效率为{end_time-start_time}')

#     return inner

# home = timer(home)
# home('太白')
# 这样你就实现了，还有一个小小的问题，现在被装饰函数的形参只是有一个形参，如果要是多个怎么办？有人说多少个我就写多少个不就行了，
# 那不行呀，你这个装饰器可以装饰N多个不同的函数，这些函数的参数是不统一的。所以你要有一种可以接受不定数参数的形参接受他们。
# 这样，你就要想到*args，**kwargs。
# import time

# def index():
#     time.sleep(2)
#     print('欢迎访问博客园主页')
#     return '访问成功'

# def home(name,age):
#     time.sleep(3)
#     print(f'欢迎访问{name}主页')

# def timer(func):
#     def inner(*args,  **kwargs):
#         start_time = time.time()
#         func(*args,  **kwargs)
#         end_time = time.time()
#         print(f'此函数的执行效率为{end_time-start_time}')

#     return inner

# home = timer(home)
# home('太白', 18)
# 这样利用*的打散与聚合的原理，将这些实参通过inner函数的中间完美的传递到给了相应的形参。

# 好将上面的代码在敲一遍。
# import time

# def home(name, age):
#     time.sleep(3)
#     print(name, age)
#     print(f'欢迎访问{name}主页')

# def timer(func):
#     def inner(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         end_time = time.time()
#         print(f'此函数的执行效率为{end_time-start_time}')

#     return inner

# home = timer(home)
# home('太白', 18)
# 如果你想给home加上装饰器，每次执行home之前你要写上一句：home = timer(home)这样你在执行home函数 home('太白',18)
# 才是真生的添加了额外的功能。但是每次写这一句也是很麻烦。所以，Python给我们提供了一个简化机制，
# 用一个很简单的符号去代替这一句话。
# import time

# def timer(func):
#     def inner(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         end_time = time.time()
#         print(f'此函数的执行效率为{end_time-start_time}')

#     return inner

# @timer  #home = timer(home)
# def home(name, age):
#     time.sleep(3)
#     print(name, age)
#     print(f'欢迎访问{name}主页')

# home('太白，18')

# 至此标准版的装饰器就是这个样子：
# def wrapper(func):
#     def inner(*args, **kwargs):
#         ret = func
#         return ret

#     return inner

# 上面这个就是标准的装饰器，完全符合代码开放封闭原则，这几行代码一定要背过，会用。
# 此时，我们要利用这个装饰器完成一个需求：简单版模拟博客园登录。此时带着学生们看一下博客园，说一下需求：
# 博客园登陆之后有几个页面，diary，comment，home，如果我要访问这几个页面，必须验证我是否已登录。 如果已经成功登录，
# 那么这几个页面我都可以无阻力访问。如果没有登录，任何一个页面都不可以访问，我必须先登录，登录成功之后，才可以访问这个页面。
# 我们用成功执行函数模拟作为成功访问这个页面，现在写三个函数，写一个装饰器，实现上述功能。


def auth(f):
    def inner(*args, **kwargs):
        login()
        if status['statu'] == False:
            ret = f(*args, **kwargs)
            return ret

    return inner


status = {
    'king': '123',
    'statu': True,
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
