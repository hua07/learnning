#生成器：大多数时候生成器和迭代器一个概念，唯一的不同就是：迭代器都是python给你提供的已经写好的工具或者通过数据转化得来的。
#生成器是需要我们自己用python代码构建的工具，最大的区别就是如此了。

#生成器的构建方式：
#在python中有三种方式来创建生成器：1、通过生成器函数。2、通过生成器推倒式。3、python内置函数或者模块提供


#生成器函数：
def func():
    print(11)
    return 22


ret = func()
print(ret)  #11 22


#将上述例子中return换成yield,这样func就不是函数了，而是一个生成器函数
def func():
    print(11)
    yield 22


ret = func()
print(ret)  # <generator object func at 0x0000020C2C4EC890>


#你会发现上面两个程序运行的结果是不一样，为什么呢，由于函数中存在yield，那么这个函数就是一个生成器函数，
#我们在执行这个函数的时候，就不在是函数的执行了。二十获取这个生成器对象，那么生成器对象如何取值呢？之前我们说了，
#生成器的真挚就是迭代器，迭代器如何取值，生成器就如何取值。所以我们可以直接执行next（）来执行以下生成器。
def func():
    print('111')
    yield 222


gener = func()  #这个时候函数不会执行，而是获取到生成器
ret = gener.__next__()  #这个时候函数才会执行
print(ret)  #yield会将func生产出来的数据222给了ret。
#输出结果：
""" 
111
222
"""


#并且我的生成器函数中可以写多个yield。
def func():
    print('111')
    yield 222
    print('333')
    yield 444


gener = func()
ret = gener.__next__()
print(ret)
ret2 = gener.__next__()
print(ret2)
ret3 = gener.__next__()
#到这里，最后一个yield执行完毕，再次__next__()程序报错
print(ret3)
#输出结果
"""
111
222
333
444
Traceback (most recent call last):
  File "e:\learngit\python全栈\day12\tempCodeRunnerFile.py", line 11, in <module>
    ret3 = gener.__next__()
StopIteration
"""


#当程序运行完最后一个yield，那么后面继续运行next（）程序会报错，一个yield对应一个next,next超过yield数量，就会报错，与迭代器一样。
#yield 与 return的区别：
#return一般在函数中只设置一个，他的作用是终止函数，并且给函数的执行者返回值。
#yield在生成器函数中的可设置多个，他并不会终止函数，获取对应yield生成的元素。
#举例：
#我们来可看一个需求：老男孩向楼下卖包子的老板订购10000个包子，包子铺老板非常实在，一下就全部都做出来了。
def eat():
    lst = []
    for i in range(1, 10000):
        lst.append('包子' + str(i))
    return lst


e = eat()
print(e)


#这样做没有问题，但是我们由于学生没有那么多，只吃了2000个包子，剩下的8000个，就只能占着一定的空间存放在一边了。
#如果老板的效率够高的话，我吃一个包子， 你做一个包子，那么这就不会占用太多空间了。
def eat():
    for i in range(1, 10000):
        yield '包子' + str(i)


e = eat()
for i in range(200):
    print(next(e))


#这两者的区别：
#第一种是直接把包子却不做出来，占用内存。第二种是吃一个生产一个，非常的节省内存，而且还可以保留上次的位置。
def eat():
    for i in range(1, 10000):
        yield '包子' + str(i)


e = eat()
for i in range(200):
    print(next(e))
for i in range(300):
    print(next(e))


# next只能获取yield生成的值，但是不能传递值。
def gen(name):
    print(f'{name} ready to eat')
    while 1:
        food = yield
        print(f'{name} start to eat {food}')


dog = gen('alex')
next(dog)
next(dog)
next(dog)


# 而使用send这个方法是可以的。
def gen(name):
    print(f'{name} ready to eat')
    while 1:
        food = yield 222
        print(f'{name} start to eat {food}')


dog = gen('alex')
next(dog)  # 第一次必须用next让指针停留在第一个yield后面
# 与next一样，可以获取到yield的值
ret = dog.send('骨头')
print(ret)


def gen(name):
    print(f'{name} ready to eat')
    while 1:
        food = yield
        print(f'{name} start to eat {food}')


dog = gen('alex')
next(dog)
# 还可以给上一个yield发送值
dog.send('骨头')
dog.send('狗粮')
dog.send('香肠')

# send和next()区别:

#         相同点：

#             send 和 next()都可以让生成器对应的yield向下执行一次。

#             都可以获取到yield生成的值。

#         不同点：

#             第一次获取yield值只能用next不能用send（可以用send(None)）。

#             send可以给上一个yield传递值。


# 对比yield 与 yield from
def func():
    lst = ['卫龙', '老冰棍', '北冰洋', '牛羊配']
    yield lst


g = func()
print(g)
print(next(g))  # 只是返回一个列表


def func():
    lst = ['卫龙', '老冰棍', '北冰洋', '牛羊配']
    yield from lst


g = func()
print(g)
# 他会将这个可迭代对象(列表)的每个元素当成迭代器的每个结果进行返回。
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''
yield from ['卫龙','老冰棍','北冰洋','牛羊配'] 
等同于：
    yield '卫龙'
    yield '老冰棍'
    yield '北冰洋'
    yield '牛羊配'
'''


#有个小坑,yield from 是将列表中的每一个元素返回,所以 如果写两个yield from 并不会产生交替的效果
def func():
    lst1 = ['卫龙', '老冰棍', '北冰洋', '牛羊配']
    lst2 = ['馒头', '花卷', '豆包', '大饼']
    yield from lst1
    yield from lst2


g = func()
for i in g:
    print(i)

#2.推导式，本节我们讲列表推导式，生成器表达式以及其他推导式，我认为推导式就是构建比较有规律的列表生成器，字典等一种
#简便的方式。那么他如何简便呢？ 看下面的例题：
#给出一个列表，通过循环向列表中添加1-10
li = []
for i in range(1, 11):
    li.append(i)
print(li)

#如果使用列表推导式会简洁许多
ls = [i for i in range(1, 11)]
print(ls)

#列表推导式分为两种：
#循环模式：[变量（加共的变量）for 变量 in iterable]
#筛选模式：[变量（加工的变量）for 变量 in iterable if 条件]

#循环模式：再做几道题：
#将10以内所有的证书的平方写入列表。
li = [i**2 for i in range(1, 11)]
print(li)
#100以内所有的偶数写入列表
ls = [i for i in range(2, 101, 2)]
print(ls)
#把从python1期到100期写入列表lst
lst = ['python' + str(i) + '期' for i in range(1, 101)]
print(lst)
lst1 = [f'python{i}期' for i in range(1, 101)]
print(lst1)

#筛选模式 ：将一个列表中大于3的元素留下来
l1 = [4, 3, 2, 6, 5, 5, 7, 8]
ls = [i for i in l1 if int(i) > 3]
print(ls)
#30以内可以被3整除的数
lst = [i for i in range(1, 31) if i % 3 == 0]
print(lst)
#过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
l = ['wusir', 'laonanhai', 'aa', 'b', 'taibai']
new_l = [i.upper() for i in l if len(i) >= 3]
print(new_l)
#找到嵌套列表中名字含有两个'e'的所有的名字（有难度）
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
name = [i for l1 in names for i in l1 if i.count('e') == 2]
print(name)

#生成器表达式：生成器表达式和列表天推导式的语法上一模一样，只是把【】换成（）就行了，比如将十以内的数的平方放到一个生成器表达式中
gen = (i**2 for i in range(10))
print(gen)
#输出结果：<generator object <genexpr> at 0x000001207710C890>

# 生成器表达式也可以进行筛选
#获取100以内能被3 整除的数
gen = (i for i in range(101) if i % 3 == 0)
for i in gen:
    print(i)
#生成器表达式和列表推导式的区别：
# 1、列表推导式比较耗内存，所有数据一次性加载到内存。而生成器表达式遵循迭代器协议，逐个产生元素。
# 2、得到的值不一样，列表推导式得到的是一个列表，生成器表达式获取的是一个生成器。
# 3、列表推导式一目了然，生成器只是一个内存地址。
#无论是生成器表达式，还是列表推导式，他只是python给你提供了一个相对简单的构造方式，因为使用推导式非常简单，所以大多数都会为之
#着迷，这个一定要慎重，推导式智能构建相对复杂的并且有规律的对象，对于没有什么规律，而且嵌套层数比较多（for循环超过层）
#这样就不建议大家用推导式构建。
#生成器的惰性机制：生成器只有在访问的时候才取值，说白了，你找人要才给你值，不找他要 ，他是不会执行的。

#字典推导式：（了解）
lst1 = ['jay', 'jj', 'meet']
lst2 = ['周杰伦', '林俊杰', '郭宝元']
dic = {lst1[i]: lst2[i] for i in range(len(lst1))}
print(dic)
#集合推导式：（了解）集合推导式可以帮我们直接生成一个集合,集合的特点;无序,不重复 所以集合推导式自带去重功能
lst = [1, 2, 3, -1, -3, -7, 9]
s = {abs(i) for i in lst}
print(s)

#构建一个这样的列表 ：[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
l1 = ['J', 'Q', 'K', 'A']
l2 = [i for i in range(2, 11)]
l2.extend(l1)
print(l2)
#第二种方式
li = [i for i in range(2, 11)] + list('JQKA')
print(li)