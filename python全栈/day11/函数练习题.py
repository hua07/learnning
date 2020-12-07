# 1、 编写一个名为 display_message() 的函数，它打印一个句子，指出你在本章学的是什么。调用这个函数，确认显示的消息正确无误。
# def display_message():
#     print(f'本章主要学习函数的基础，以及简单应用')

# display_message()

# 2、 编写一个名为 favorite_book() 的函数，其中包含一个名为 title 的形参。这个函数打印一条消息，如 One of my favorite
# books is Alice in Wonderland 。调用这个函数，并将一本图书的名称作为实参传递给它。
# def favorite_book(title):
#     print(f'one of my favorite books is {title.title()}')

# favorite_book('python')

# 3、 编写一个名为 make_shirt() 的函数，它接受一个尺码以及要印到 T 恤上的字样。这个函数应打印一个句子，
# 概要地说明 T 恤的尺码和字样。使用位置实参调用这个函数来制作一件 T 恤；再使用关键字实参来调用这个函数。
# def make_shirt(size, word):
#     print(f'这是一个印有{word.title()}的{size}码的T恤')

# make_shirt(23, 'i love python')
# make_shirt(word='i love you', size=22)
# 4、 修改函数 make_shirt() ，使其在默认情况下制作一件印有字样 “I love Python” 的大号 T 恤。调用这个函数来制作如下 T 恤：
# 一件印有默认字样的大号 T恤、一件印有默认字样的中号 T 恤和一件印有其他字样的 T 恤（尺码无关紧要）。
# def make_shirt(size, word='i love python'):
#     print(f'这是一个印有{word.title()}的{size}码的T恤')
# 5、 编写一个名为 describe_city() 的函数，它接受一座城市的名字以及该城市所属的国家。这个函数应打印一个简单的句子，
# 如 Reykjavik is in Iceland 。给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认
# 国家。
# def describe_city(city,country='中国'):
#     print(f'{city.title()} is in {country}。')

# describe_city('beijing')
# describe_city('nanjing')
# describe_city('londen','英国')

# 6、 编写一个名为 city_country() 的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于这样的字符串：
# "Santiago, Chile" 。至少使用三个城市 - 国家对调用这个函数，并打印它返回的值。
# def describe_city(city,country='中国'):
#     msg = (f'{city.title()}, {country}。')
#     return msg
# print(describe_city('山东'),type(describe_city('山东')))
# 7、 编写一个名为 make_album() 的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，
# 并返回一个包含这两项信息的字典。使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。给函数 make_album() 添加一个可选形参，以便能够存储专辑包含的歌曲数。如果调用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
# def make_album(name,album):
#     dic = {}
#     dic[name] = album
#     return dic
# print(make_album('周杰轮','黑色毛衣'))
# print(make_album('林俊杰','9527'))
# print(make_album('陈奕迅','爱情呼叫转移'))
# 8、 简述普通参数、指定参数、默认参数、动态参数的区别
#实参角度：有位置参数，关键字参数，混合参数（需要注意的是位置参数永远在前）
#形参角度：有位置参数，*arges，默认参数，仅限关键字参数，**kwarges 需要注意的是在形参中的顺序就像现在排序一样不能改变
#“ *　”　＊的作用在形参角度是聚合，在实参角度是打散。
# 9、 写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def my_len(s):
#     if len(s) > 5:
#         print(f'{s}的长度大于5')
#     else:
#         print(f'{s}的长度小于5')

# msg = 'asdfljk'
# my_len(msg)
# 10、写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。
# def my_len(s):
#     for i in s:
#         if ' ' in i:
#             return print('你输入的对象里包含空格')
#     print('你输入的对象里不包含空格')

# msg = 'asdfljk '
# my_len(msg)
# 11、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
# def my_len(s):
#     if len(s) > 2:
#         s = s[:2]
#     return s

# print(my_len('king'))

# 12、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def check_index(ite):
#     """ 定义函数检查传入对象的所有奇数索引位对应元素，并将其作为新列表返回给调用者"""
#     lis = []
#     for i in range(1,len(ite),2):
#         lis.append(ite[i])
#     return lis

# print(check_index('namgeaskdjflkj'))
# 13、写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# PS:字典中的value只能是字符串或列表
# def my_len(dic):
#     for key,value in dic.items():
#         if len(value) > 2:
#             dic[key] = value[:2]
#     return dic
# dic1 = {'name':'king','age':'9','hobby':'mwnv'}
# print(my_len(dic1))


# 14、 写函数，利用递归获取斐波那契数列中的第 10 个数，并将该值返回给调用者。
def recur_fibo(n):
    """递归函数
   输出斐波那契数列"""
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


print(recur_fibo(9))


def sum(num):
    n = 0
    a = num
    dic = {}
    while a > 0:
        if n == 0:
            dic[n] = 0
        elif n == 1:
            dic[n] = 1
        else:
            dic[n] = dic[n - 1] + dic[n - 2]
        n += 1
        a -= 1
    return dic[num - 1]


print(sum(10))
