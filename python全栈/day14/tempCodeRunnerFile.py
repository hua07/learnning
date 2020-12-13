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
    
f  = my_time(index)
f()