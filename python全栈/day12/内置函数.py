#python提供了68个内置函数。方便我们使用，省去我们写的常用功能
# 常用函数的功能示例：
#abs（）函数 ，返回一个数字类型（可以是正数，负数，浮点数，长整形）的绝对值
# print(abs(-32))
# print(abs(-0.776))
# print(abs(35))
# print(abs(3.175))
# print(abs(1546465456879876512313156456))

#all(iterable)函数，接收一个可迭代对象，如果其中所有的元素都是True，或者该可迭代对象中没有元素，则返回True否则返回False
from types import FunctionType
from typing import Iterable

ls1 = [1, 2, 3, None]
print(all(ls1))  #可迭代对象中包含 None, 所以返回False
ls2 = [1, 2, 3, 0]
print(all(ls2))  #可迭代对象中包含 0 ,所以返回False
ls3 = [1, 2, 3, '']
print(all(ls3))  #可迭代对象中包含 '' ,所以返回False
ls6 = [1, 2, 3, []]
print(all(ls6))
ls4 = []
print(all(ls4))  #空的列表里面没有任何元素，返回True
ls5 = ()
print(all(ls5))  #空的元组里面没有任何元素，返回True

#any(iterable)函数，如果iterable的任意一个元素不为False就返回True

# eval:执行字符串代码，并返回最终结果
eval('2+2')
n = 81
eval('n+4')
eval('print(6666)')

# exec:执行字符串类型的代码
s = """ 
for i in [1,2,3]:
    print(i)"""
exec(s)

# hash:获取一个对象（可哈希对象：int，str，bool，tuple）的哈希值
print(hash(12333))
print(hash(255))
print(hash('1234'))
print(hash('arg'))
print(hash(True))
print(hash(False))
print(hash((
    1,
    2,
    3,
)))

# help:函数用于查看函数或模块的用途的详细说明。
# print(help(list))
# print(help(str.split))

#callable:函数用于检查一个对象是否是可调用的。如果返回true，object仍然可能调用失败，
# 但如果放回false，调用对象ojbect绝对不会成功。
name = 'alex'


def func():
    pass


print(callable(name))
print(callable(func))

# int:函数用于将一个字符串或数字转换为整型。
print(int())
print(int('12'))
print(int(3.6))
print(int('1010', base=2))

# float:函数用于将整数和字符串转换成浮点数。
# complex：函数用于创建一个值为real+imag*j d 复数或转换一个字符串数为复数，如果第一个参数为字符串
# 则不需要指定第二个参数。
print(float(3))
print(complex(1, 2))

# bin:将十进制转换成二进制字符串并返回
# otc：将十近制转换成八进制字符串并返回
# hex：将十进制转化成十六进制字符串并返回
print(bin(10), type(bin(10)))
print(oct(10), type(oct(10)))
print(hex(10), type(hex(10)))

# divmod:计算除数与被除数的结果，返回一个包含商和余数的元组（a//b,a%b)
# round:保留浮点数的小数位数，默认保留整数。
# pow:求x**y次幂（三个参数为x**y的结果对z取余）
print(divmod(7, 2))
print(round(7 / 3, 2))
print(round(7 / 3))
print(round(3.32567, 3))
print(pow(2, 3))
print(pow(2, 3, 3))

# bytes:用于不同编码之间的转化。
s = '你好'
bs = s.encode('utf-8')
print(bs)
s1 = bs.decode('utf-8')
print(s1)
bs = bytes(s, encoding='utf-8')
print(bs)
b = '你好'.encode('gbk')
b1 = b.decode('utf-8')
print(b1.encode('utf-8'))

# ord 输入字符找该字符编码的位置
# cha 输入位置数字找出其对应的字符
print(ord('a'))
print(ord('中'))
print(chr(97))
print(chr(20013))

# repr:返回一个对象的srting形式（原形毕露）
name = 'taibai'
print('我叫%r' % name)
print(repr('{"name":"alex"}'))
print('{"name":"alex"}')
# all:可迭代对象中，全都是true是true
# any:可迭代对象中，有一个ture就是true
print(all([1, 2, True, 0]))
print(any([1, ',0']))
print(all(set()))
print(any([]))

#  内置函数二(以下的每个函数都是重点中的重点必须都熟练使用)
# print()输出
# int()
# str()
# bool()
# set()
# list():将一个可迭代对象转换成列表
# tuple()：将一个可迭代对象转换成元组
# dict():通过相应的方式创建字典
l1 = list('abcd')
print(l1)
tul = tuple('abcd')
print(tul)

# abs()返回绝对值
i = -5
print(abs(i))
# sum()求和
print(sum([1, 2, 3]))
print(sum((1, 2, 3), 100))
# min()求最小值
print(min([1, 2, 3]))
ret = min([
    1,
    2,
    -5,
], key=abs)
print(ret)

# max()最大值与最小值用法相同。
# reversed()将一个序列反转，返回反转序列的迭代器reversed示例
l = reversed('你好')
print(list(l))
ret = reversed([1, 4, 3, 7, 9])
print(list(ret))

# bytes()把字符串转换成bytes类型
# zip()拉链方法：函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组
# 然后返回由这些元组组成的内容，如果各个迭代器的元素个数不一致，则按照长度最短的返回。
lst1 = [
    1,
    2,
    3,
]
lst2 = ['a', 'b', 'c', 'd']
lst3 = (11, 12, 13, 14, 15)
for i in zip(lst1, lst2, lst3):
    print(i)

# sorted排序函数
# 语法：sorted(iterable,key=None,reverse=False)
# Iterable:可迭代对象
# key:排序规则（排序函数）在sorted内部会将可迭代对象中的每一个元素传递给这个函数的参数，
# 根据函数的运算结果进行排序
# reverse:是否是倒叙，true倒叙 false正序
lst = [1, 3, 2, 5, 4]
lst2 = sorted(lst)
print(lst)  #使用sorted函数，原列表不会改变
print(lst2)  #返回的一个新的经过排序的列表

lst3 = sorted(lst, reverse=True)
print(lst3)  #倒叙

# 字典使用sorted排序
dic = {1: 'a', 3: 'c', 2: 'b'}
print(sorted(dic))  #字典排序返回的就是排序后的key

# 和函数组合使用
lst = [
    '天龙八部',
    '西游记',
    '红楼梦',
    '三国演义',
    '水浒传',
]


def func(s):
    return len(s)


print(sorted(lst, key=func))

# 和lambda组合使用
lst = [
    '天龙八部',
    '西游记',
    '红楼梦',
    '三国演义',
    '水浒传',
]
print(sorted(lst, key=lambda s: len(s)))

lst = [
    {
        'id': 1,
        'name': 'alex',
        'age': 18
    },
    {
        'id': 2,
        'name': 'wusir',
        'age': 17
    },
    {
        'id': 3,
        'name': 'taibai',
        'age': 16
    },
]
new_lst = sorted(lst, key=lambda s: s['age'])
print(new_lst)

# filter筛选过滤
# filter(functoin,tierable)
# function:用来筛选的函数，在filter中会自动把tierable中的元素传递给function，然后根据function返回
# true或false来判断是否保留此数据
# iterable：可迭代对象

lst = [
    {
        'id': 1,
        'name': 'alex',
        'age': 18
    },
    {
        'id': 2,
        'name': 'wusir',
        'age': 17
    },
    {
        'id': 3,
        'name': 'taibai',
        'age': 16
    },
]
ls = filter(lambda e: e['age'] > 16, lst)
print(list(ls))

# map映射函数
# 语法：map(faunction,iterable)可以对可迭代对象中的每一个元素映射，分别取执行FunctionType
# 计算列表中每个元素的平方，返回新列表：
lst = [1, 2, 3, 4, 5]


def func(s):
    return s * s


mp = map(func, lst)
print(map)
print(list(mp))

# 改写成lambda
lst = [1, 2, 3, 4, 5]
print(list(map(lambda s: s * s, lst)))

# reduce
from functools import reduce


def func(x, y):
    return x + y


# reduce 的使用方式
# reduce(函数名，可迭代对象) #这两个参数必须都要有，缺一不可
ret = reduce(func, [3, 4, 5, 6, 7])
print(ret)  #结果 25
# reduce的作用是先把列表中的前两个元素取出计算出一个值然后临时保存着，然后用这个临时保存的值和列表中
# 第三个取出的值进行计算，求出一个新的值将最开始临时保存的值覆盖掉，然后再用这个新的临时值和第四个值计算，
# 以此类推

#注意：我们放进去的可迭代对象没有更改
# 以上这个例子我们使用送用sum就可以完全的实现了，我现在有【1，2，3，4，】想让列表中的数变成1234，就要
# 用到reduce了。
# 普通函数版：
from functools import reduce

# def func(x,y):
#     return x*10+y
# l = reduce(func,[1,2,3,4])
# print(l)

#匿名函数版
l1 = reduce(lambda x, y: x * 10 + y, [
    1,
    2,
    3,
    4,
])
print(l1)
