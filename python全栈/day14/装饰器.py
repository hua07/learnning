# 装饰器：在不改变原被装饰的函数的源代码以及调用方式下，为其添加额外的功能。
def index():
    print('欢迎访问博客园主页')


#需求介绍：你现在在某公司的开发部任职，领导给你一个业务需求让你完成：让你写代码测试上面函数的执行效率。
#需求分析：你想要测试此函数的执行效率，你应该怎么做？应该在此函数执行前记录一个时间，执行完毕之后记录一个时间，这个时间差
# 就是具体此函数的执行效率。那么执行时间如何获取呢？可以利用time模块，有一个time.time()功能。
import time


def index():
    print('欢迎访问博客园主页')


start_time = time.time()
index()
end_time = time.time()
print(f'此函数的执行效率为{end_time-start_time}')

# 由于index函数自由一行代码，执行效率太快了，所以我们利用time模块的一个sleep模拟一下。
import time


def index():
    time.sleep(2)
    print('欢迎访问博客园主页')


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


def my_time(func):
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f'此函数的执行效率为{end_time-start_time}')

    return inner


f = my_time(index)
f()