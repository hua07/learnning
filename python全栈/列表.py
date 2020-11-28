li = [100, '太白', '[1,2,3],True']
#索引
print(li[0], type(li[0]))
print(li[1], type(li[1]))
print(li[-1])

#练习题
li = [1, 3, 2, 'a', 4, 'b', 5, 'c']
""" 
通过对li列表切片形成新的列表l1，l1 = [1,3,2]
通过对li列表切片形成新的列表l2, l2 = ['a',4,'b']
通过对li列表切片形成新的列表l3, l3 = [3,'a','b']
通过对li列表切片形成新的列表l4, l4 = ['b','a',3] """
l1 = li[:3]
l2 = li[3:6]
l3 = li[1:-2:2]
l4 = li[-3:0:-2]
print(l1, l2, l3, l4)

#列表的创建
#方式一 l1 = list()
#方式二 l1 = list('adfwerasdfa')
#练习题：
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
""" 
计算列表的长度并输出
列表中追加元素"seven",并输出添加后的列表
请在列表的第1个位置插入元素"Tony",并输出添加后的列表
请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
请删除列表中的元素"ritian",并输出添加后的列表
请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
请删除列表中的第2至4个元素，并输出删除元素后的列表 """
# count = len(li)
# print(count)
# li.append('sever')
# print(li)
# li.insert(0,'Tony')
# print(li)
# li[1] = 'kelly'
# print(li)
# l2=[1,"a",3,4,"heart"]
# li.extend(l2)
# print(li)
# s = "qwert"
# li.extend(s)
# print(li)
# li.remove('ritian')
# print(li)
# word = li.pop(2)
# print(word,li)
# del li[1:4]
# print(li)

#列表的嵌套练习题
l1 = [1, 2, 'taibai', [
    1,
    'alex',
    3,
]]
""" 
1, 将l1中的'taibai'变成大写并放回原处。
2，给小列表[1,'alex',3,]追加一个元素,'老男孩教育'。
3，将列表中的'alex'通过字符串拼接的方式在列表中变成'alexsb'
 """
# l1[2] = l1[2].upper()
# l1[-1].append('老男孩教育')
# l1[-1][1] += 'sb'
# print(l1)

lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# 将列表lis中的"tt"变成大写（用两种方式）。
# lis[3][2][1][0] = lis[3][2][1][0].upper()
# lis[3][2][1][0] = 'TT'

# 将列表中的数字3变成字符串"100"（用两种方式）。
# lis[1] = 100
# lis[1] += 97
# 将列表中的字符串"1"变成数字101（用两种方式）。
# lis[3][2][1][-1] = 101
# lis[3][2][1][-1] = int(lis[3][2][1][-1]+'01')
# print(lis)

#range 类似与列表的一个自制数字范围的列表。
# r = range(10)
# print(r)
# for i in r:
#     print(i)
#range同样可以使用索引切片（步长）
# range多与for循环结合
# l1 =[1,2,3,'alex','太白']
#利用for循环和range将l1列表的所有索引打印出来
# for i in range(len(l1)):
#     print(i)
# l = [1, 2, 'a']
# l.extend('wang')
# print(l)
# l = [1, 2, 'a']
# l.insert(1, 'name')
# print(l)
