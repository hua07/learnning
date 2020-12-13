#python提供了68个内置函数。方便我们使用，省去我们写的常用功能
# 常用函数的功能示例：
#abs（）函数 ，返回一个数字类型（可以是正数，负数，浮点数，长整形）的绝对值
# print(abs(-32))
# print(abs(-0.776))
# print(abs(35))
# print(abs(3.175))
# print(abs(1546465456879876512313156456))

#all(iterable)函数，接收一个可迭代对象，如果其中所有的元素都是True，或者该可迭代对象中没有元素，则返回True否则返回False
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
