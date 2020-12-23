#  写一个电影投票程序，
# from typing import ItemsView

# lst = ['复仇者联盟4', '驯龙高手33', '金瓶梅', '老男孩', '大话西游']

# # 要求用户给每一个电影投票，最终将该用户投票信息公布出来。
# # 用户可以持续投票，用户输入序号，进行投票。比如输入序号 1，给金瓶梅投票
# # 每次投票成功，显示给哪部电影投票成功。
# # 退出投票程序后，要显示最终投票数。
# # 要求输出格式为：{'金瓶梅'：99，'复仇者联盟'：22，。。。。。}
# def movie_lst():
#     a = 1
#     for i in lst:
#         print(f'{a},{lst[a-1]}')
#         a += 1

# dic = {}
# for key in lst:
#     dic[key] = 0

# while 1:
#     movie_lst()
#     num = input(f'请输入你喜欢的电影编号(q或Q退出)：')
#     if num.upper() == 'Q':
#         break
#     else:
#         dic[lst[int(num) - 1]] += 1
#         print(f'已为{lst[int(num)-1]}投票成功')
# print(dic)

# 有一个文件t1.txt里面的内容为：
# id,name,age,phone,job
# 1,alex,22,13651054608,IT 2,wustr,23,13304320533,Tearcher 3,taibai,18,1333235322,It
# 利用文件操作，将其构造成如下数据类型。
# [{'id':'1','name':'alex','age':'22','phone':'13651054608','job':'IT'......}]
# with open('t1.txt', mode='r', encoding='utf-8') as f:
#     msg1 = f.readline().strip().split(',')
#     msg2 = f.readline().strip().split(' ')
# lst = []
# dic = {}
# for i in msg2:
#     ls_msg2 = i.split(',')
#     for n in range(len(msg1)):
#         dic[msg1[n]] = ls_msg2[n]
#     lst.append(dic)
# print(lst)

#按要求完成下列转化，
list3 = [
    {
        'name': 'alex',
        'hobby': '抽烟'
    },
    {
        'name': 'alex',
        'hobby': '喝酒'
    },
    {
        'name': 'alex',
        'hobby': '烫头'
    },
    {
        'name': 'alex',
        'hobby': 'Massage'
    },
    {
        'name': 'wusir',
        'hobby': '喊麦'
    },
    {
        'name': 'wusir',
        'hobby': '街舞'
    },
]
# list4 = [
#     {
#         'name': 'alex',
#         'hobby_list': [
#             '抽烟',
#             '喝酒',
#             '烫头',
#             'Massage',
#         ]
#     },
#     {
#         'name': 'wusit',
#         'hobby_list': [
#             '喊麦',
#             '街舞',
#         ]
#     },
# ]
#将list3这种数据类型转化成list4类型，你写的代码必须只可拓展
# 比如list3数据再加一个这样的字典{'name':'wusir','hobby':'溜达'}，
# list4{'name':'wusir','hobby_list':['喊麦','街舞','溜达']}，
# 或者list3 增加一个字典{'name':'太白','hobby':'开车'}，
# list4{'name':'太白','hobby_list':['开车']}，
# 无论按照要求加多少数据，你的代码都可以转化，如果不支持拓展，则得4分，支持拓展则10分。
# def change(lis):
# dic = {}
# for i in list3:
#     if i['name'] not in dic:
#         dic[i['name']] = list[i['hobby']]
#     else:
#         dic[i['name']].append(i['hobby'])
# print(dic)
list4 = []
for i in list3:
    for j in list4:
        if i['name'] == j['name']:
            j['hobby_lis'].append(i['hobby'])
            break
        else:
            j['name'] = i['name']
            j['hobby_lis'] = list(i['hobby'], )

print(list4)