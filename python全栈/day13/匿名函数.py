#匿名函数：顾名思义就是没有名字的函数，使用lambda来定义一个匿名函数，
func = lambda a, b: a + b
print(func(1, 2))
#函数名 = lambda 参数：返回值
# 1、此函数不是没有名字，他是有名字的，他的名字就是你给其设置的变量，比如func
# 2、lambda定义匿名函数的关键字，相当于函数的def。
# 3、lambda后面直接加形参，形参加多少都可以，只要用逗号隔开就行。
# func1 = lambda a,b,*args,sex='man',c,**kwargs:kwargs
# print(func1(3,4,c=666,name= 'alex'))
# 4、返回值在冒号之后设置，返回值和正常的函数一样，可以是任意数据类型。
# 5、匿名函数不管多复杂，只能写一行，且逻辑结束后直接返回数据。

# 写匿名函数：接收一个可切片的数据，返回索引为0与2的对应的元素（元组形式）
# tu = lambda s:(s[0],s[2])
# print(tu('adfghd'))

# 写匿名函数：接收两个int参数，将较大的数据返回。
# my_max = lambda x,y: x if x>y else y
# print(my_max(3,9))

#内置函数：必须熟练掌握:abs()enumerate()filter()map()min()open()range()print()len()list()dict()str()reversed()set()
#sorted()sum()tuple()type()zip()dir()

# l = reversed('你好')  # l 获取到的是一个生成器
# print(l, type(l))
# print(list(l))
# ret = reversed([1, 4, 3, 7, 9])
# print(list(ret))  # [9, 7, 3, 4, 1]

# abs()返回绝对值
# i = -5
# print(abs(i))
# #sum 求和
# print(sum([1,2,3]))
# print(sum((1,2,3),100))

# #min()最小值
# print(min([1,2,3]))  # 返回此序列最小值
# ret = min([1,2,-5,],key=abs)  # 按照绝对值的大小，返回此序列最小值
# print(ret)
# # 加key是可以加函数名，min自动会获取传入函数中的参数的每个元素，然后通过你设定的返回值比较大小，返回最小的传入的那个参数。
# print(min(1,2,-5,6,-3,key=lambda x:abs(x)))  # 可以设置很多参数比较大小
# dic = {'a':3,'b':2,'c':1}
# print(min(dic,key=lambda x:dic[x]))
# # x为dic的key，lambda的返回值（即dic的值进行比较）返回最小的值对应的键

# # reversed() 将一个序列翻转, 返回翻转序列的迭代器 reversed 示例:
# l = reversed('你好') # l 获取到的是一个生成器
# print(list(l))#['好', '你']
# ret = reversed([1, 2, 3, 7, 9])
# print(list(ret)) #[9, 7, 3, 2, 1]

# bytes() 把字符串转换成bytes类型

# s = '你好太白'
# print(s,type(s))
# bs = s.encode('utf-8')
# print(bs,type(bs))
# # 结果:b'\xe4\xbd\xa0\xe5\xa5\xbd\xe5\xa4\xaa\xe7\x99\xbd' <class 'bytes'>

# s1 = bs.decode('utf-8')
# print(s1,type(s1))
# # 结果: 你好太白 <class 'str'>

# s = '你好'
# bs = bytes(s,encoding='utf-8')
# print(bs,type(bs))
# # 将字符串转换成字节

# bs1 = str(bs,encoding='utf-8')
# print(bs1,type(bs1))
# # 将字节转换成字符串

# zip() 拉链方法。函数用于将可迭代的对象作为参数,将对象中对应的元素打包成一个个元组,

# 然后返回由这些元祖组成的内容,如果各个迭代器的元素个数不一致,则按照长度最短的返回，
# lst1 = [1, 2, 3]
# lst2 = ['a', 'b', 'c', 'd']
# lst3 = (11, 12, 13, 14, 15)

# for i in zip(lst1, lst2, lst3):
#     print(i)
#输出结果：
""" 
(1, 'a', 11)
(2, 'b', 12)
(3, 'c', 13) 
"""

# sorted排序函数
# 语法:sorted(iterable,key=None,reverse=False)

# iterable : 可迭代对象

# key: 排序规则(排序函数),在sorted内部会将可迭代对象中的每一个元素传递给这个函数的参数.根据函数运算的结果进行排序

# reverse :是否是倒叙,True 倒叙 False 正序

# lst = [1, 3, 2, 5, 4]
# lst2 = sorted(lst)
# print(lst)  #原列表不会改变
# print(lst2)  #返回的新列表是经过排序的

# lst3 = sorted(lst, reverse=True)
# print(lst3)  #倒叙
""" 
输出结果:
[1, 3, 2, 5, 4]
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
 """
# 字典使用sorted排序

# dic = {1: 'a', 3: 'c', 2: 'b'}
# print(sorted(dic))  # 字典排序返回的就是排序后的key
""" 
输出结果:
[1,2,3]
 """

# 和函数组合使用

# 定义一个列表,然后根据一元素的长度排序
# lst = ['天龙八部', '西游记', '红楼梦', '三国演义']

# 计算字符串的长度
# def func(s):
#     return len(s)

# print(sorted(lst, key=func))

# 结果:
# ['西游记', '红楼梦', '天龙八部', '三国演义']

# 和lambda组合使用

# lst = ['天龙八部', '西游记', '红楼梦', '三国演义']

# print(sorted(lst, key=lambda s: len(s)))

# 结果:
#  ['西游记', '红楼梦', '天龙八部', '三国演义']

# lst = [
#     {
#         'id': 1,
#         'name': 'alex',
#         'age': 18
#     },
#     {
#         'id': 2,
#         'name': 'wusir',
#         'age': 17
#     },
#     {
#         'id': 3,
#         'name': 'taibai',
#         'age': 16
#     },
# ]
# lst2 = sorted(lst, key=lambda s: s.get('id'))
# print(lst2)
# 按照年龄对学生信息进行排序

# print(sorted(lst, key=lambda e: e['age']))

# 结果:
""" [{
    'id': 3,
    'name': 'taibai',
    'age': 16
}, {
    'id': 2,
    'name': 'wusir',
    'age': 17
}, {
    'id': 1,
    'name': 'alex',
    'age': 18
}]
 """

# filter筛选过滤
# 语法: filter(function,iterable)

# function: 用来筛选的函数,在filter中会自动的把iterable中的元素传递给function,
# 然后根据function返回的True或者False来判断是否保留此项数据

# iterable:可迭代对象

# lst = [{'id':1,'name':'alex','age':18},
#         {'id':1,'name':'wusir','age':17},
#         {'id':1,'name':'taibai','age':16},]

# ls = filter(lambda e:e['age'] > 16,lst)

# print(list(ls))

# 结果:
# [{'id': 1, 'name': 'alex', 'age': 18},
#  {'id': 1, 'name': 'wusir', 'age': 17}]

# 映射函数

# 语法: map(function,iterable) 可以对可迭代对象中的每一个元素进映射,分别取执行function

# 计算列表中每个元素的平方,返回新列表

# lst = [1, 2, 3, 4, 5]

# def func(s):

#     return s * s

# mp = map(func, lst)

# print(mp, type(mp))

# print(list(mp))

# 改写成lambda

# lst = [1, 2, 3, 4, 5]

# print(list(map(lambda s: s * s, lst)))

# 计算两个列表中相同位置的数据的和

# lst1 = [1, 2, 3, 4, 5]
# lst2 = [2, 4, 6, 8, 10]

# print(list(map(lambda x, y: x + y, lst1, lst2)))

# 结果:

# [3, 6, 9, 12, 15]

# from functools import reduce
# def func(x,y):
#     return x + y

# reduce 的使用方式:
# reduce(函数名,可迭代对象)  # 这两个参数必须都要有,缺一个不行

# ret = reduce(func,[3,4,5,6,7])
# print(ret)  # 结果 25
# reduce的作用是先把列表中的前俩个元素取出计算出一个值然后临时保存着,
# 接下来用这个临时保存的值和列表中第三个元素进行计算,求出一个新的值将最开始
# 临时保存的值覆盖掉,然后在用这个新的临时值和列表中第四个元素计算.依次类推

# 注意:我们放进去的可迭代对象没有更改
# 以上这个例子我们使用sum就可以完全的实现了.我现在有[1,2,3,4]想让列表中的数变成1234,就要用到reduce了.
# 普通函数版
# from functools import reduce

# def func(x,y):

#     return x * 10 + y
# 第一次的时候 x是1 y是2  x乘以10就是10,然后加上y也就是2最终结果是12然后临时存储起来了
# 第二次的时候x是临时存储的值12 x乘以10就是 120 然后加上y也就是3最终结果是123临时存储起来了
# 第三次的时候x是临时存储的值123 x乘以10就是 1230 然后加上y也就是4最终结果是1234然后返回了

# l = reduce(func,[1,2,3,4])
# print(l)

# 匿名函数版
# l = reduce(lambda x,y:x*10+y,[1,2,3,4])
# print(l)

# 在Python2.x版本中recude是直接 import就可以的, Python3.x版本中需要从functools这个包中导入

# 龟叔本打算将 lambda 和 reduce 都从全局名字空间都移除, 舆论说龟叔不喜欢lambda 和 reduce

# 最后lambda没删除是因为和一个人写信写了好多封,进行交流然后把lambda保住了.