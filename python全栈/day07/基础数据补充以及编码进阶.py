# #captalize,swapcase,title
# name = 'wang king'
# print(name,capitalize())#首字母大写
# print(name.swapcase())#大小写翻转
# print(name.title())#每个单词的首字母大写

# #内同居中，总长度，空白处填充
# a1 = 'assj'
# ret1 = a1.center(20,'*')
# print(ret1)

# #寻找字符串中的元素是否存在
# a2 = 'adlfjals234sdfj'
# ret2 = a2.find('fjdk',1,6)
# print(ret1)#返回找到的元素的索引，如果找不到返回-1

# ret3 = a2.index('fjdk',4,6)
# print(ret3) #返回找到的元素的索引，找不到报错。

# tu = (1)
# print(tu,type(tu)) # 1 <class 'int'>
# tu1 = ('alex')
# print(tu1,type(tu1)) # 'alex' <class 'str'>
# tu2 = ([1, 2, 3])
# print(tu2,type(tu2)) # [1, 2, 3] <class 'list'>

# tu = (1,)
# print(tu,type(tu))  # (1,) <class 'tuple'>
# tu1 = ('alex',)
# print(tu1,type(tu1))  # ('alex',) <class 'tuple'>
# tu2 = ([1, 2, 3],)
# print(tu2,type(tu2) # ([1, 2, 3],) <class 'tuple'>

# #index：通过元素索引（可切片），找到第一个元素就返回，找不到该元素即报错。
# tu = ('太白', [1, 2, 3]), 'wusir', '女神'）
# print(tu.cou('太白')) # 0

# #count：获取某元素在列表中出现的次数
# tu1 = ('太白', '太白', 'wusit', '吴超')
# print(tu1.count('太白')) # 2

# #count 统计某个元素在列表次数
# a = ['q', 'w', 'q', 'r', 't', 'y']
# print(a,count('q')) # 2

# #index 找出列表中某个值第一个匹配的索引位置
# b = ['q', 'w', 'r', 't', 'r' ]
# print(b.index('r')) # 2

# #sort 用于在原位置对列表进行排序
# c = ['q', 'w', 'r', 't', 'r' ]
# c.sort() #它没有返回值，所以只能打印c
# print(c)

# #reverse 将列表中的元素反向存放
# d = [2, 1, 3, 4, 5]
# d.reverse() # 它没有返回值，所以只能打印d
# print(d)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(l1 + l2) #[1, 2, 3, 4, 5, 6]
# print(l1 * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

#有一个列表l1 = [11, 22,33, 44, 55]请用循环把索引为奇数的对应元素删除
#第一种方法
# l1 = [11, 22,33, 44, 55]
# l2 = []
# for i in range(len(l1)):
#     if i % 2 == 0:
#         l2.append(l1[i])
# l1 = l2
# print(l1)
#第二种方法
# l1 = [11, 22, 33, 44, 55,]
# for i in range(len(l1))[::-1]:
#     if i % 2 == 1:
#         l1.pop(i)
# print(l1)
#第三种方法
# l1 = [11, 22, 33, 44, 55,]
# del l1[1::2]
# print(l1)

# dict:字典的增删改查的方法
#popitem 3.5版本之前，popitem为随机删除，3.6之后为删除最后一个，有返回值
# dic = {'name': '太白', 'age': 18}
# ret = dic.popitem()
# print(ret,dic) # ('age', 18) {'name': '太白'}

# # update
# dic = {'name': '太白', 'age': 18}
# dic.update(sex='男', height=175)
# print(dic) # {'name': '太白', 'age': 18, 'sex': '男', 'height': 175}

# dic = {'name': '太白', 'age': 18}
# dic.update([(1, 'a'),(2, 'b'),(3, 'c'),(4, 'd')])
# print(dic) # {'name': '太白', 'age': 18, 1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# dic1 = {"name":"jin","age":18,"sex":"male"}
# dic2 = {"name":"alex","weight":75}
# dic1.update(dic2)
# print(dic1) # {'name': 'alex', 'age': 18, 'sex': 'male', 'weight': 75}
# print(dic2) # {'name': 'alex', 'weight': 75}

# fromkeys:创建一个字典：字典的所有键来自一个可迭代对象，字典的值使用同一个值
# dic = dict.fromkeys('abcd','太白')
# print(dic) # {'a': '太白', 'b': '太白', 'c': '太白', 'd': '太白'}
#
# dic = dict.fromkeys([1, 2, 3],'太白')
# print(dic) # {1: '太白', 2: '太白', 3: '太白'}

# 这里有一个坑，就是如果通过fromkeys得到的字典的值为可变的数据类型，那么你的小心了。
# dic = dict.fromkeys([1, 2, 3], [])
# dic[1].append(666)
# print(id(dic[1]),id(dic[2]),id(dic[3]))  # {1: [666], 2: [666], 3: [666]}
# print(dic)  # {1: [666], 2: [666], 3: [666]}

# 循环字典，改变字典大小的问题
#来，先来研究一个小题，有如下字典：

# dic = {'k1':'太白','k2':'barry','k3': '白白', 'age': 18} 请将字典中所有键带k元素的键值对删除。
# 那么拿到这个题，有人说我一个一个删除，这是不行的，因为这个字典只是举个例子，里面的元素不确定，
# 所以你要怎么样？你要遍历所有的键，符合的删除，对吧？ 嗯，终于上套了，哦不，上道了，请开始你的表演。
# dic = {'k1': '太白', 'k2': 'barry', 'k3': '白白', 'age': 18}
# new_dic = {}
# for i in dic.keys():
#     if 'k' not in i:
#         new_dic.setdefault(i, dic[i])
# dic = new_dic
# print(dic)

#把unicode转换成utf-8的编码显示
# name = 'wang 臻'
# old_name = name.encode('utf-8')
# print(old_name)

# #把unicode转换成gbk编码显示
# word = 'hello,世界'
# new_word = word.encode('gbk')
# print(new_word)  # b'hello,\xca\xc0\xbd\xe7'

# #非unicode编码之间的转换
# word1 = new_word.decode('gbk')
# print(word1)  # hello,世界
# word2 = word1.encode('utf-8')
# print(word2)  # b'hello,\xe4\xb8\x96\xe7\x95\x8c'
