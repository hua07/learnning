l1 = [1, 2, 3, [22, 33]]
l2 = l1
l1.append(666)
print(l1,l2)#他们两个都会改变，因为他们的id地址是一样的
print(id(l1))
print(id(l2))
print(l1 is l2)