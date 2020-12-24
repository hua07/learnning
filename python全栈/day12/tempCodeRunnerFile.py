from functools import reduce

# def func(x,y):
#     return x*10+y
# l = reduce(func,[1,2,3,4])
# print(l)

#匿名函数版
l1 = reduce(lambda x,y:x*10+y ,[1,2,3,4,])
print(l1)
