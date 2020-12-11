# 由于闭包这个概念比较难以理解，尤其是初学者来说，相对难以掌握，所以我们通过示例去理解学习闭包。

# 给大家提个需求，然后用函数去实现：完成一个计算不断增加的系列值的平均值的需求。

# 例如：整个历史中的某个商品的平均收盘价。什么叫平局收盘价呢？就是从这个商品一出现开始，每天记录当天价格，然后计算他的平均值：平均值要考虑直至目前为止所有的价格。

# 比如大众推出了一款新车：小白轿车。

# 第一天价格为：100000元，平均收盘价：100000元

# 第二天价格为：110000元，平均收盘价：（100000 + 110000）/2 元

# 第三天价格为：120000元，平均收盘价：（100000 + 110000 + 120000）/3 元

# ........
#我的做法：
# day_price = []
# price = int(input('请输入商品今日价格：'))
# day_price.append(price)
# sum_price = (sum(day_price))/len(day_price)

# 老师的解法：
series = []


def make_averager(new_value):
    series.append(new_value)
    total = sum(series)
    return total / len(series)


print(make_averager(100000))
print(make_averager(110000))
print(make_averager(120000))

# 从上面的例子可以看出，基本上完成了我们的要求，但是这个代码相对来说是不安全的，因为你的这个series列表是一个全局变量，
# 只要是全局作用域的任何地方，都可能对这个列表进行改变。
series = []


def make_averager(new_value):
    series.append(new_value)
    total = sum(series)
    return total / len(series)


print(make_averager(100000))
print(make_averager(110000))
series.append(666)  # 如果对数据进行相应改变，那么你的平均收盘价就会出现很大的问题。
print(make_averager(120000))


# 我们用闭包的思想改一下这个代码
def make_averager():

    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()
print(avg(100000))
print(avg(110000))
print(avg(120000))

# 大家仔细看一下这个代码，我是在函数中嵌套了一个函数。那么avg 这个变量接收的实际是averager函数名，也就是其对应的内存地址，我执行了三次avg 也就是执行了三次averager这个函数。那么此时你们有什么问题？

# 肯定有学生就会问，那么我的make_averager这个函数只是执行了一次，为什么series这个列表没有消失？反而还可以被调用三次呢？这个就是最关键的地方，也是闭包的精华所在。我给大家说一下这个原理，以图为证：

#     上面被红色方框框起来的区域就是闭包，被蓝色圈起来的那个变量应该是make_averager()函数的局部变量，它应该是随着make_averager()函数的执行结束之后而消失。但是他没有，是因为此区域形成了闭包，series变量就变成了一个叫自由变量的东西，averager函数的作用域会延伸到包含自由变量series的绑定。也就是说，每次我调用avg对应的averager函数 时，都可以引用到这个自用变量series，这个就是闭包。

# 闭包的定义：

#     1. 闭包是嵌套在函数中的函数。

#     2. 闭包必须是内层函数对外层函数的变量（非全局变量）的引用。


# 如何判断判断闭包？举例让同学回答：
# 例一：
def wrapper():
    a = 1

    def inner():
        print(a)

    return inner


ret = wrapper()

# 例二：
a = 2


def wrapper():
    def inner():
        print(a)

    return inner


ret = wrapper()
print(ret())

# 例三：


def wrapper(a, b):
    def inner():
        print(a)
        print(b)

    return inner


a = 2
b = 3
ret = wrapper(a, b)


# 以上三个例子，最难判断的是第三个，其实第三个也是闭包，如果我们每次去研究代码判断其是不是闭包，有一些不科学，
# 或者过于麻烦了，那么有一些函数的属性是可以获取到此函数是否拥有自由变量的，如果此函数拥有自由变量，
# 那么就可以侧面证明其是否是闭包函数了（了解）：
def make_averager():

    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()
# 函数名.__code__.co_freevars 查看函数的自由变量
print(avg.__code__.co_freevars)  # ('series',)
# 当然还有一些参数，仅供了解：

# 函数名.__code__.co_freevars 查看函数的自由变量
print(avg.__code__.co_freevars)  # ('series',)
# 函数名.__code__.co_varnames 查看函数的局部变量
print(avg.__code__.co_varnames)  # ('new_value', 'total')
# 函数名.__closure__ 获取具体的自由变量对象，也就是cell对象。
# (<cell at 0x0000020070CB7618: int object at 0x000000005CA08090>,)
# cell_contents 自由变量具体的值
print(avg.__closure__[0].cell_contents)  # []

# 闭包的作用：保存局部信息不被销毁，保证数据的安全性。

# 闭包的应用：

# 1、可以保存一些非全局变量但是不易被销毁、改变的数据。

# 2、装饰器。