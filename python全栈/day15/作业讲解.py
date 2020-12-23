# def wrapper(f):
#     def inner(*args,**kwargs):
#         print(111)
#         ret = f(*args,**kwargs)
#         print(222)
#         return ret
#     return inner
# @wrapper #func = wrapper(func)
# def func():
#     print('in func')
# func()


#为函数写一个装饰器，把函数执行5遍返回
def wrapper(f):
    def inner(*args, **kwargs):
        for i in range(5):
            f(*args, **kwargs)

    return inner


@wrapper
def more():
    print('一次性打印5遍')


more()
