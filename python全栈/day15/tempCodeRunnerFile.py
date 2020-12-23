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
            j['hobby_list'].append(i['hobby'])
            break
    else:
         list4.append({'name':i['name'],'hobby_list':[i['hobby'],]})

print(list4)