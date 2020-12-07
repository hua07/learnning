l1 = [11, 22, 33, 44, 55, 66]
obj = iter(l1)  #l1.__iter__()
print(next(obj))  # l1.__next__()
print(next(obj))  # l1.__next__()
print(next(obj))  # l1.__next__()
print(next(obj))  # l1.__next__()
print(next(obj))  # l1.__next__()
print(next(obj))  # l1.__next__()
print(next(obj))  # l1.__next__()

#利用while循环模拟for循环对可迭代对象进行曲直的机制。
l2 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
#首先将l2列表转换成迭代器
idj = iter(l2)
while 1:
    try:
        print(next(l1))
    except StopIteration:
        break
