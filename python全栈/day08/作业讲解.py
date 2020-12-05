#水仙花数是一个三位数，三位数的每一位的三次方的和还等于这个数，那这个数就是一个水仙花数。
# num = input('请输入一个三位数：').strip()
# s = 0
# for i in num:
#     s += int(i)**3
# if s == int(num):
#     print('你输入的是一个水仙花数')
# else:
#     print('你输入的不是水仙花数')

#把列表中所有周姓的人的信息删除：
# lst = ['周老二', '周星星', '麻花藤', '周扒皮', '李子柒']
#第一种方法，根据索引倒着删除
# for i in range(len(lst))[::-1]:
#     if lst[i].strip().startswith('周'):
#         lst.pop(i)
# print(lst)

#第二种方法，可以新建一个列表，把不符合周姓的人的信息都放到新的列表中。
# lst = ['周老二', '周星星', '麻花藤', '周扒皮', '李子柒']
# li = []

# for i in lst:
#     if i.strip().startswith('周'):
#         pass
#     else:
#         li.append(i)
# print(li)

#车牌区域划分，现给出以下车牌，根据车牌的信息，分析出给省的车牌持有量
# cars = ['鲁A32444', '鲁B12333', '京B8989M', '黑C46555', '沪B25041']
# locals = {'沪': '上海', '黑': '黑龙江', '鲁': '山东', '鄂': '湖北', '湘': '湖南', '京': '北京'}
# #要求输出结果为：{'黑龙江'：2， '山东':1, '北京':1}
# count_local = {}
# for key in locals:
#     for car in cars:
#         if car.strip()[0] == key:
#             if locals[key] in count_local:
#                 count_local[locals[key]] += 1
#             else:
#                 count_local[locals[key]] = 1
# print(count_local)

#第二种方法：要弄清楚每个对象之间的关系，这样操作起来才不会走弯路。
# cars = ['鲁A32444', '鲁B12333', '京B8989M', '黑C46555', '沪B25041']
# locals = {'沪': '上海', '黑': '黑龙江', '鲁': '山东', '鄂': '湖北', '湘': '湖南', '京': '北京'}
# dic = {}
# for car in cars:
#     if locals[car.strip()[0]] not in dic:
#         dic[locals[car.strip()[0]]] = 1
#     else:
#         dic[locals[car.strip()[0]]] += 1
# print(dic)

#第三种方法：需要对字典的get方法灵活运用
# cars = ['鲁A32444', '鲁B12333', '京B8989M', '黑C46555', '沪B25041']
# locals = {'沪': '上海', '黑': '黑龙江', '鲁': '山东', '鄂': '湖北', '湘': '湖南', '京': '北京'}
# dic = {}
# for i in cars:
#     dic[locals[i[0]]] = dic.get(locals[i[0]],0) + 1
# print(dic)