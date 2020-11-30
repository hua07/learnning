#集合是无序的，不重复的数据集合，它里面的元素是可哈希的（不可变类型），但是集合本身是不可哈希
#所以集合做不了字典的键，以下是集合两个重要的两点：
#1.去重，把一个列表变成集合，就自动去重了。
#2.关系测试，测试两组数据之间的交集、差集、并集等关系。
#一、集合的创建。
# set1 = set({1, 2, 'name'})
# set2 = {1, 2, 'wang'}
# print(set1, set2)

#二、集合的增。
#第一种方法：add 直接增加
# set3 = {'alex', 'wusir', 'ritian', 'egon', 'barry'}
# set3.add('景女神')
# set3.add(('name', 'wang', 'age'))
# print(set3)

#第二种方法：update 迭代着增加
# set3.update('A')
# print(set3)
# set3.update('老师')
# print(set3)
# set3.update([1, 2, 3])
# print(set3)

#三、集合的删
# set4 = {'alex', 'wusir', 'ritian', 'egon', 'barry'}
# set4.remove('alex')  #remove根据元素来删除
# print(set4)
# set4.pop()  #pop随机删除一个元素
# print(set4)
# set4.clear()  #清空集合
# print(set4)
# del set4  #删除集合
# print(set4)

#四、集合的其他操作：
#交集（& 或者 intersection）
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1 & set2)
# print(set1.intersection(set2))
# #并集（|或者union）
# print(set1 | set2)
# print(set1.union(set2))
# #差集（-或者difference)
# print(set1 - set2)
# print(set1.difference(set2))
# #反交集（^或者symmetric_difference)
# print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# #子集与超集
# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5, 6}
# print(set1 < set2)
# print(set1.issubset(set2))

# set1 = {'太白金星','景女神','武大','三粗','alexsb','吴老师'}
# set1.add('wang')
# print(set1)
# set1.remove('wang')
# print(set1)

l1 = [1, 2, 3, [22, 33]]
l2 = l1
l1.append(666)
print(l1, l2)  #他们两个都会改变，因为他们的id地址是一样的
print(id(l1))
print(id(l2))
print(l1 is l2)