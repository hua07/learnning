# 你如何将三个数据（这三个数据都是可迭代对象类型）s1 = 'alex',l1 = [1, 2, 3, 4], tu1 = ('武sir', '太白', '女神',)
# 的每一元素传给动态参数*args？（就是args最终得到的是 ('a','l','e','x', 1, 2, 3, 4,'武sir', '太白', '女神',）

#课间考一道题：位置参数最终顺序：*args，默认参数，仅限关键字参数，**kwargs
# def foo(a,b,*args,c,sex=None,**kwargs):
#     print(a,b)
#     print(c)
#     print(sex)
#     print(args)
#     print(kwargs)
# foo(1,2,3,4,c=6)
# foo(1,2,sex='男',name='alex',hobby='old_woman')
# foo(1,2,3,4,name='alex',sex='男')
# foo(1,2,c=18)
# foo(2, 3, [1, 2, 3],c=13,hobby='喝茶')
# foo(*[1, 2, 3, 4],**{'name':'太白','c':12,'sex':'女'})

# li = []
# a = 1
# def func():
#     li.append(1)
#     global a
#     a += 1
# func()
# print(li)
# print(a)

#nonlocal的总结：1、不能改变全局变量。2、在局部作用域中，对父级作用域（或者更外层作用域非全局作用域）的变量进行引用和修改，
# 并且引用的哪层，从那层及以下此变量全部发生改变。
# def add_b():
#     b = 42

#     def do_global():
#         b = 10
#         print(b) #输出10

#         def dd_nonlocal():
#             nonlocal b
#             b = b + 20
#             print(b)# 输出30

#         dd_nonlocal()
#         print(b) # 输出30

#     do_global()
#     print(b) # 输出42

# add_b()

#写一个函数，计算你传入函数的所有的数字的和。
# def my_sum(*args):
#     count = 0
#     for i in args:
#         count += int(i)
#     return count

# print(my_sum(5, 3, 45, 2))

#创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians()的函数，这个函数打印列表中的每个魔术师的名字。
# def show_magicians(lis):
#     for name in lis:
#         print(name)
# magicians_lis = ['mack', 'king', 'wang']
# show_magicians(magicians_lis)

#了不起的魔术师：在你完成上题的程序三，编写一个名为make_great()函数，对魔术师列表进行修改，在每个魔术师的名字中都加入
#字样“the Great“。调用函数show_magicians()，确认魔术师确实变了。
# def show_magicians(lis):
#     for name in lis:
#         print(name)

# def make_great(lis):
#     new_lis = []
#     for name in lis:
#         name = f'the Great {name}'
#         new_lis.append(name)
#     lis = new_lis
#     return lis

# magicians_lis = ['mack', 'king', 'wang']
# new_magicians_lis = make_great(magicians_lis)
# show_magicians(new_magicians_lis)

#不变的魔术师：修改你的完成上题的程序，在调用函数make_great()时，向它传递魔术师列表的副本，由于不想修改原始列表，请返回
#修改后的列表，并将其储存到另一个列表中。分别使用这两个列表来调用show_magicians()，确认一个列表包含的是原来的魔术师名字
#而另一个列表包含的是添加了字样“the Great“的魔术师名字
# def show_magicians(lis):
#     for name in lis:
#         print(name)

# def make_great(lis):
#     new_lis = []
#     for name in lis:
#         name = f'the Great {name}'
#         new_lis.append(name)
#     return new_lis

# magicians_lis = ['mack', 'king', 'wang']
# new_magicians_lis = make_great(magicians_lis[:])
# show_magicians(new_magicians_lis)
# show_magicians(magicians_lis)