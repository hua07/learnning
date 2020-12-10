# def func1():
#     print('in func1')

# def func2(x):
#     print('in func2')
#     return x

# def func3(y):
#     print('in func3')
#     return y

# print(func2(func1))
# ret = func2(func1)  # in func2
# ret()  #in func1
# ret2 = func3(func2)  #in func3
# ret3 = ret2(func1)  #in func2
# ret3()  #in func1

#看代码写结果：
# l1 = []

# def func(args):
#     l1.append(args)
#     return l1

# print(func(1))  #[1]
# print(func(2))  #[1,2]
# print(func(3))  #[1,2,3]

#看代码写结果
# def extendlist(val, list=[]):
#     list.append(val)
#     return list

# list1 = extendlist(10)
# list2 = extendlist(123, [])
# list3 = extendlist('a')
# print(f'list1={list1}') #list1=[10, 'a']
# print(f'list2={list2}') #list2=[123]
# print(f'list3={list3}') #list3=[10, 'a']
#出现上述结果的主要原因是：定义函数的行参是一个列表，它存储在一个默认空间中，当函数执行完一次之后，还会存在，但当你传递给
#函数一个新的列表时，这个列表的传递是在临时空间开辟的。当函数执行完毕，临时空间也会关闭，列表随之消失。

#使用while模拟for循环：
# li = list(range(100))
# dir = iter(li) #模拟for循环最为关键的一步，就是把可迭代对象转换成迭代器。然后利用迭代器的next()方法会返回stopiteration解决
# while 1:
#     try:
#         print(next(dir))
#     except:
#         StopIteration

#写函数，传入一个参数，放回它的阶乘。
# def factorial(n):
#     if n == 0:
#         return 1
#     return factorial(n-1)*n

# fac1 = factorial(8)
# print(fac1)

#利用递归编写一个斐波那契数列，
# def fib(n):
#     if n <= 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# for i in range(20):
#     print(fib(i), end=' ')

#写代码完成99乘法表
# li = range(1,10)
# for n in li:
#     for m in range(1,n+1):
#         print(f'{n}*{m}={n*m}')