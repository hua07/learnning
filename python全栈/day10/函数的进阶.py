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

#8-12三明治：编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个函数只有一个形参（它收集函数调用中提供的所有食材）
#并打印一条消息，对顾客点的三明治进行概述。调用这个函数三次，每次都提供不同数量的实参。
# def make_sandwich(*arges):
#     for i in arges:
#         print(f'已向你点的三明治添加{i}')

# make_sandwich('洋葱','大蒜','番茄','土豆','牛肉','辣椒')
# make_sandwich('turkey', 'apple slices', 'honey mustard')
# make_sandwich('peanut butter', 'strawberry jam')

# 8-14编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接收制造商和型号，还接受任意数量的关键字实参。这样调用
# 这个函数：提供必不可少的信息，以及两个名称值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：
# car = make_car('subaru','outback',clolr = 'blue',tor_package = True)
# 打印返回的字典，确认正确处理了所有的信息。
# def make_car(manufacturer, model, **kwargs):
#     """ 创建一个字典存储汽车的所有信息 """
#     car_dict = {
#         'manufactruer': manufacturer.title(),
#         'model': model.title(),
#     }
#     car_dict.update(kwargs)
#     return car_dict

# my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(my_outback)

# my_accord = make_car('honda',
#                      'accord',
#                      year=1991,
#                      color='white',
#                      headlights='popup')
# print(my_accord)

#函数的有点之一是，使用他们可将代码块与主程序分离。通过给函数指定描述性的名称，可让主程序容易理解的多。你还可以更进一步，将
#函数存储在被称为模块的独立文件中，再将模块导入程序中。import语句允许在当前运行的程序文件中使用模块中代码。
#通过 将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上。这还能让 你在众多不同的程序中重用函数。
#将函数存储在独立文件中后，可与其他程序员共享这些文件而不是整个程序。知道如何导入函数还能让你使用其他程序员编写的函数函数裤。
#导入模块的方法有多种，下面对每种都作简要的介绍。

# a = 100
# def func():
#     global a    # 加了个global表示不再局部创建这个变量了. 而是直接使用全局的a
#     a = 28
# print(a)
# func()
# print(a)

# lst = ["麻花藤", "刘嘉玲", "詹姆斯"]
# def func():
#     lst.append("⻢云")
#     # 对于可变数据类型可以直接进⾏访问
#     print(lst)
# print(lst)
# func()
# print(lst)

# a = 10
# def func1():
#     a = 20
#     def func2():
#         a = 30
#         def func3():
#             nonlocal a # nonlocal 只修改上一层变量,如果上一层中没有变量就往上找一层,只会找到函数的最外层,不会找到全局进行修改
#             a = 40
#             print(a)
#         func3()
#         print(a)
#     func2()
#     print(a)
# func1()
# print(a)
#输出的结果是：
# 40
# 40
# 20
# 10

# a = 10
# def func1():
#     a = 20
#     def func2():
#         def func3():
#             nonlocal a # nonlocal 只修改上一层变量,如果上一层中没有变量就往上找一层,只会找到函数的最外层,不会找到全局进行修改
#             a = 40
#             print(a)
#         func3()
#         print(a)
#     func2()
#     print(a)
# func1()
# print(a)
#输出的结果：
# 40
# 40
# 40
# 10

a = 1


def fun_1():
    a = 2

    def fun_2():
        nonlocal a
        a = 3

        def fun_3():
            a = 4
            print(a)  # 4

        print(a)  # 3
        fun_3()
        print(a)  # 3

    print(a)  # 2
    fun_2()
    print(a)  # 3


print(a)  # 1
fun_1()
print(a)  # 1
#输出结果：
# 1
# 2
# 3
# 4
# 3
# 3
# 1
