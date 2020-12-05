# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic['k4'] = 'v4'
# dic.setdefault('k4','v4')
# 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic['k1'] = 'alex'
# dic.update(k1 = 'alex')
# dic.update({'k1':'alex'})
# 请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic['k3'].append(44)
# dic['k3'].insert(3,44)
# 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# dic['k3'].insert(0,18)
# print(dic)

# dic1 = {
#     'name': ['alex', 2, 3, 5],
#     'job': 'teacher',
#     'oldboy': {
#         'alex': ['phthon1', 'python2', 100]
#     }
# }
#1、将name对应的列表追加一个元素'wusir'
# dic1['name'].append('wusir')
#2、将name对应的对应的列表中的alex首字母大写
# dic1['name'][0] = dic1['name'][0].title()
#3、oldboy对应的字典加一个键值对'老男孩','linux'
# dic1['oldboy']['老男孩']='linux'
# dic1.update(老男孩 = 'linux')
# dic1.update({'老男孩':'linux'})
# dic1.update([('老男孩','linux')])
# dic1.setdefault('老男孩', 'wusir')
#4、将oldboy对应的字典中的alex对应的列表中的python2删除
# dic1['oldboy']['alex'].pop(1)
# print(dic1)

#有字符串'k:1|k1:2|k2:3|k3:4'处理成字典{'k1':1, 'k1':2, 'k2':3, k3:4}
# dic = {}
# msg = 'k:1|k1:2|k2:3|k3:4'
# new_msg = msg.split('|')
# for i in new_msg:
#     key,value = i.split(':')
#     dic.setdefault(key.strip(),int(value))

# print(new_msg)
# print(dic)

#字典的创建方法：
# dic = {'小王':'12345678910','小弓':'15423698710'} #常用方法
# dic1 = dict([('name','word'),('say','something')])
# print(dic)
# print(dic1)

#字典的注意事项：
#字典的key是唯一的，且必须是不可变的数据类型：int,str,tuple,bool,float

#字典的键值对的增加：
# score_dict = {
#     '小明': 96,
#     '小红':98,
#     '小刚':94
# }
# score_dict.setdefault('小丽',100) # 可以通过setdefault方法追加键值对，没有就增加，有则不变
# score_dict['小朋'] = 99 # 也可以直接增加键值对，没有就增加，有则更改
# print(score_dict)

#访问字典里的值：
# score_dict = {
#     '小明': 96,
#     '小红':98,
#     '小刚':94
# }
# print(score_dict['小红']) #可以直接通过索引来查，如果没有你要查询的键，就会报错
# some_one = score_dict.get('小李')# 也可以使用get方法，有返回值，如果没有你要查询的键，就返回None
# print(some_one)

#删除字典里的键值对
#pop（）根据键来删除，有返回值，
# score_dict = {
#     '小明': 96,
#     '小红':98,
#     '小刚':94
# }
# word1 = score_dict.pop('小红','没有此键') # 可以设置返回值，如果有此键，就返回键对应的值，
# word2 = score_dict.pop('小李','没有此键') # 如果没有此键，就返回设置返回值。

# print(word1,word2)

#字典的方法介绍：
# 1. clear, 删除字典内所有的元素
# dic = {
#     '小明': 98
# }
# dic.clear()
# print(dic)
# 使用clear方法后，字典dic变成了空字典，有人可能会问，这种清空字典的方法和直接将空字典赋值给变量dic有什么区别

# dic = {
#     '小明': 98
# }
# dic = {}
# print(dic)
# 程序最终输出的结果同样是{},dic 变成了空字典。两种方式，变量dic都变成了空字典，但意义不同，使用clear方法，
# 字典在内存中的地址没有发生变化，但是第二种方法，变量dic指向了一个新的空字典，原来的字典被垃圾回收机制回收了，
# 我们可以通过输出变量的内存地址来验证

# dic1 = {
#     '小明': 98
# }
# print("使用clear方法前，dic1内存地址为", id(dic1))
# dic1.clear()
# print(dic1)
# print("使用clear方法后，dic1内存地址为", id(dic1))

# print("\n\n分割线"+"*"*30 + "\n"*2)

# dic2 = {
#     '小明': 98
# }
# print("赋值空字典之前，dic1内存地址为", id(dic2))
# dic2 = {}
# print(dic2)
# print("赋值空字典之后，dic1内存地址为", id(dic2))
# 程序输出结果为

# 使用clear方法前，dic1内存地址为 4352796640
# {}
# 使用clear方法后，dic1内存地址为 4352796640

# 分割线******************************

# 赋值空字典之前，dic1内存地址为 4729716312
# {}
# 赋值空字典之后，dic1内存地址为 4729716168
# clear是清空字典，而将一个空字典赋值给变量，并不是清空，只是修改了变量的引用而已。

# 2. copy， 返回字典的浅复制
# dic1 = {
#     '小明': 98
# }

# dic2 = dic1.copy()

# print(dic1)
# print(dic2)
# 程序输出结果为

# {'小明': 98}
# {'小明': 98}
# dic2是dic1的复制品，他们的内容一模一样，在python中，还有一个模块，可是实现数据的复制功能，它就是copy模块

# import copy

# dic1 = {
#     '小明': 98
# }

# dic2 = copy.copy(dic1)

# print(dic1)
# print(dic2)
# 这两段代码都实现了浅复制，浅复制是一种危险的复制，建议你不要使用，因为这种复制并没有创建新的对象，因此，
# 你对dic2的修改会影响到dic1

# dic1 = {
#     'stu': ['小明', '小红']
# }

# dic2 = dic1.copy()
# dic2['stu'].append('小刚')

# print(dic1)
# 程序输出结果为

# {'stu': ['小明', '小红', '小刚']}
# 关于对象的深拷贝和浅拷贝，会有专门的章节进行讲解

# 3. fromkeys,以指定key创建一个新的字典
# stu_dict = dict.fromkeys(['小明', '小刚'], 90)
# print(stu_dict)
# 程序输出结果为

# {'小明': 90, '小刚': 90}
# fromkeys方法接受两个参数，第一个参数是序列，可以是列表，也可以是元组，方法将以这个序列里的元素做key，
# 生成新的字典。value由第二个参数来决定，我在代码里传入参数90，所有key所对应的value就都是90，如果不传这个参数，
# 默认value为None

# 4. get，返回指定key的值
# get方法，是一种安全的获取value的方法，如果key不存在，则返回default，default可以由你来指定，如果你不指定，
# 则默认为None

# empty_dict = {}

# print(empty_dict.get('python'))
# print(empty_dict.get('python', 100))
# 程序输出结果

# None
# 100
# 5. items(),成对返回所有key和value
# items()方法通常被用在字典遍历的场景下

# score_dict = {
#     '小明': 96,
#     '小刚': 98,
#     '小红': 94
# }

# for key, value in score_dict.items():
#     print(key, value)
# items()方法返回一个可迭代对象，使用for循环遍历这个可迭代对象时，得到的是一个元组，元组内包含key和 value

# 下面的代码向你揭示items()方法返回的对象的本质面目

# from collections import Iterable
# score_dict = {
#     '小明': 96,
#     '小刚': 98,
#     '小红': 94
# }

# iter_obj = score_dict.items()
# print(isinstance(iter_obj, Iterable))

# for item in iter_obj:
#     print(item)
# 程序输出结果为

# True
# ('小明', 96)
# ('小刚', 98)
# ('小红', 94)
# 6. keys,返回字典所有的key
# score_dict = {
#     '小明': 96,
#     '小刚': 98,
#     '小红': 94
# }

# keys = score_dict.keys()

# print(keys, type(keys))

# for key in keys:
#     print(key)
# 程序输出结果

# dict_keys(['小明', '小刚', '小红']) <class 'dict_keys'>
# 小明
# 小刚
# 小红
# keys()方法在py2.7里，返回的是包含了所有key的列表，但在py3.6中，返回的是可迭代对象，遍历这个对象，
# 就可以得到字典所有的key

# 7. values,返回字典所有value
# score_dict = {
#     '小明': 96,
#     '小刚': 98,
#     '小红': 94
# }

# values = score_dict.values()

# print(values, type(values))

# for value in values:
#     print(value)
# values()方法返回的是一个可迭代对象，遍历这个可迭代对象，可以获得字典所有的value

# 8. setdefault，为key设置对应的默认值
# 这个方法和get有些类似，如果key不存在，则增加新的键值对，如果key已经存在，则不做任何操作

# score_dict = {
#     '小明': 96,
#     '小刚': 98,
#     '小红': 94
# }

# score_dict.setdefault('小明', 100)    # 小明这个key已经存在，因此这行语句不产生任何影响
# score_dict.setdefault('小丽', 97)     # 小丽这个key不存在，增加新的键值对，key为小丽，value为97

# print(score_dict)
# 程序输出结果

# {'小明': 96, '小刚': 98, '小红': 94, '小丽': 97}
# 9. update 更新字典
# 一般的使用模式是dic1.update(dic2)，将dic2的内容更新到dic1中

# score_dict = {
#     '小明': 96,
#     '小刚': 98,
#     '小红': 94
# }

# score_dict2 = {
#     '小明': 100,
#     '小丽': 98,
# }

# score_dict.update(score_dict2)
# print(score_dict)
# 如果一个key，在两个字典中都存在，则value的最终结果取决于dic2

# 10. pop 删除键值对
# 不论是使用del 还是使用pop方法删除字典里的键值对，如果key不存在都会引发KeyError异常，pop与del的不同之处在于，
# pop会返回所删除键值对的value

# score_dict = {
#     '小明': 96,
#     '小刚': 98,
#     '小红': 94
# }

# del score_dict['小红']
# print(score_dict.pop('小明'))

# print(score_dict)
# 程序输出结果

# 96
# {'小刚': 98}

#字典实践：
# score_dict = {
#     '小明': 96,
#     '小刚': 98,
#     '小红': 94
# }
# print(score_dict['小丽']) #会报错
# 使用一个在字典中不存在的key，会引发异常，为了避免这种异常，通常有两种方法，先来说第一种方法
# score_dict = {
#     '小明': 96,
#     '小刚': 98,
#     '小红': 94
# }

# print(score_dict.get('小丽')) #有键对应的值就返回值，没有就返回None

# 现在要求你统计每个单词出现的次数，并将单词与单词出现的次数存储到字典中你可以这样实现代码
# lst = ['green', 'white', 'black', 'white', 'green', 'green']
# dic = {}
# for i in lst:
#     dic.setdefault(i,0)
#     dic[i] += 1
# print(dic)

#使用items()方法遍历字典
# score_dict = {
#     '小明': 96,
#     '小刚': 98,
#     '小红': 94
# }

# for key, value in score_dict.items():
#     print(key, value)
#item()方法返回一个可迭代对象，使用佛循环遍历这个可迭代对象时，得到的是一个元组，远组内包含key和value

# 1. 字典基本操作
# 字典内容如下

# dic = {'python': 95, 'java': 99, 'c': 100}
# 用程序解答下面的题目

# 字典的长度是多少
# print(len(dic))
# 请修改'java' 这个key对应的value值为98
# dic.update(java = 98)
# print(dic)
# 删除 c 这个key
# dic.pop('c')
# print(dic)
# 增加一个key-value对，key值为 php, value是90
# dic.setdefault('php',90)
# print(dic)
# 获取所有的key值，存储在列表里
# lis_key = list(dic.keys())
# print(lis_key)
# 获取所有的value值，存储在列表里
# lis_value = list(dic.values())
# print(lis_value)
# 判断 javascript 是否在字典中
# print(dic.get('javascript','不在字典中'))

# 获得字典里所有value 的和
# dic_value = dic.values()
# print(sum(dic_value))
# 获取字典里最大的value
# print(max(dic.values()))
# 获取字典里最小的value
# print(min(dic.values()))
# 字典 dic1 = {'php': 97}， 将dic1的数据更新到dic中
# dic1 = {'php': 97}
# dic.update(dic1)
# print(dic)

# 第1题，len(dic),结果为3
# 第2题，dic['java'] = 98,对字典里value的修改，必须通过key才可以
# 第3题，del dic['c']
# 第4题，dic['php'] = 90
# 第5题，lst = list(dic.keys())
# 第6题，lst = list(dic.values())
# 第7题，'javascript' in dic
# 第8题，sum(dic.values())
# 第9题，max(dic.values())
# 第10题，min(dic.values())
# 第11题，dic.update(dic1)

# 2. 字典应用（买水果）
# 小明去超市购买水果，账单如下

# 苹果  32.8
# 香蕉  22
# 葡萄  15.5
# 请将上面的数据存储到字典里，可以根据水果名称查询购买这个水果的费用

# 很简单哦，用水果名称做key，金额做value，创建一个字典

# info = {
#     '苹果':32.8,
#     '香蕉': 22,
#     '葡萄': 15.5
# }
# 3. 字典应用（买水果2）
# 小明，小刚去超市里购买水果

# 小明购买了苹果，草莓，香蕉，一共花了89块钱，，小刚购买了葡萄，橘子，樱桃，一共花了87块钱

# 请从上面的描述中提取数据，存储到字典中，可以根据姓名获取这个人购买的水果种类和总费用。

# 以姓名做key，value仍然是字典

# info = {
#     '小明': {
#         'fruits': ['苹果', '草莓', '香蕉'],
#         'money': 89
#     },
#     '小刚': {
#         'fruits': ['葡萄', '橘子', '樱桃'],
#         'money': 87
#     }
# }