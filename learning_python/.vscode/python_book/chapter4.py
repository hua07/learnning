""" 
动手试一试
4-1 比萨 ：想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用for 循环将每种比萨的名称都打印出来。
修改这个for 循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。对于每种比萨，都显示一行输出，如“I like pepperoni pizza”。
在程序末尾添加一行代码，它不在for 循环中，指出你有多喜欢比萨。输出应包含针对每种比萨的消息，还有一个总结性句子，如“I really love pizza!”。
4-2 动物 ：想出至少三种有共同特征的动物，将这些动物的名称存储在一个列表中，再使用for 循环将每种动物的名称都打印出来。
修改这个程序，使其针对每种动物都打印一个句子，如“Adogwould makea great pet”。
在程序末尾添加一行代码，指出这些动物的共同之处，如打印诸如“Any oftheseanimals would makea great pet!”这样的句子。
"""
# 4-1示例

pizzas = ['Marinara','Margherita','Romana','Napoletana','Siciliana']
for i in pizzas:
    print(i,'is my favorite food.\n')
print('i really like pizza.')

#4-2 示例

animals = ['dog','cat','bird']
for i in animals:
    if i in ['dog']:
        print(i,'是人类最忠诚的伙伴')
    elif i in ['cat']:
        print(i,'最常见的宠物')
    else:
        print(i,'最喜欢的动物')
print('你最喜欢那个动物呢')


""" 
4-3 数到20 ：使用一个for 循环打印数字1~20（含）。
4-4 一百万 ：创建一个列表，其中包含数字1~1 000 000，再使用一个for 循环将这些数字打印出来（如果输出的时间太长，按Ctrl+ C停止输出，或关闭输出窗口）。
4-5 计算1~1 000 000的总和 ：创建一个列表，其中包含数字1~1 000 000，再使用min() 和max() 核实该列表确实是从1开始，到1 000 000结束的。另外，对这个列表
调用函数sum() ，看看Python将一百万个数字相加需要多长时间。
4-6 奇数 ：通过给函数range() 指定第三个参数来创建一个列表，其中包含1~20的奇数；再使用一个for 循环将这些数字都打印出来。
4-7 3的倍数 ：创建一个列表，其中包含3~30内能被3整除的数字；再使用一个for 循环将这个列表中的数字都打印出来。
4-8 立方 ：将同一个数字乘三次称为立方。例如，在Python中，2的立方用2**3 表示。请创建一个列表，其中包含前10个整数（即1~10）的立方，再使用一个for 循
环将这些立方数都打印出来。
4-9 立方解析 ：使用列表解析生成一个列表，其中包含前10个整数的立方。

 """

# 4-3
numbers = list(range(1,21))
for i in numbers:
    print(i,end='、')

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)

# 4-4
digits = range(1,1000001)
print(min(digits))
print(max(digits))
print(sum(digits)) 

odd_numbers = range(1,20,2)
for i in odd_numbers:
    print(i) 

odd_numbers = [i for i in range(1,20,2)]
print(odd_numbers)
print(max(odd_numbers))
print(min(odd_numbers))
print(sum(odd_numbers))

odd_number = range(1,31)
for i in odd_number:
    if i % 3 == 0:
        print(i)

odd_numbers = [i for i in range(3,31,3)]
print(odd_numbers)

for i in range(1,11):
    digits = i**3
    print(digits)

digits = [i**3 for i in range(1,11)]
print(digits)




""" 
4-10 切片 ：选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
打印消息“Thefirst threeitems in thelistare:”，再使用切片来打印列表的前三个元素。
打印消息“Threeitems fromthe middle ofthelistare:”，再使用切片来打印列表中间的三个元素。
打印消息“Thelast threeitems in thelistare:”，再使用切片来打印列表末尾的三个元素。
4-11 你的比萨和我的比萨 ：在你为完成练习4-1而编写的程序中，创建比萨列表的副本，并将其存储到变量friend_pizzas 中，再完成如下任务。
在原来的比萨列表中添加一种比萨。
在列表friend_pizzas 中添加另一种比萨。
核实你有两个不同的列表。为此，打印消息“My favorite pizzasare:”，再使用一个for 循环来打印第一个列表；打印消息“My friend's favorite pizzasare:”，再使用一
个for 循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。

 """
pizzas = ['Marinara','Margherita','Romana','Napoletana','Siciliana']
for i in pizzas:
    print(i,'is my favorite food') 
print('Thefirst threeitems in thelistare:',pizzas[0:3])
print('Threeitems fromthe middle ofthelistare:',pizzas[1:4])
print('Thelast threeitems in thelistare:',pizzas[-1:-4])


my_pizzas = ['Marinara','Margherita','Romana','Napoletana','Siciliana']
friend_pizzas = my_pizzas[:]
my_pizzas.append('kele')
friend_pizzas.append('xuebi')
for i in my_pizzas:
    print('\t',i)
for l in friend_pizzas:
    print('\n',l) 

""" 
4-13 自助餐 ：有一家自助式餐馆，只提供五种简单的食品。
请想出五种简单的食品，并将其存储在一个元组中。
使用一个for 循环将该餐馆提供的五种食品都打印出来。
尝试修改其中的一个元素，核实Python确实会拒绝你这样做。
餐馆调整了菜单，替换了它提供的其中两种食品。请编写一个这样的代码块：
给元组变量赋值，并使用一个for 循环将新元组的每个元素都打印出来。
 """

menu = ('蛋炒饭','拉面','盖饭','馒头','咸菜')
for i in menu:
    print(i)
menu = ('蛋炒饭','拉面','盖饭','大盘鸡','烧烤',)
for l in menu:
    print("\n",l)

a = ['mary','had','a','little','lab']
for i in range(len(a)):
    print(i,a[i],end = '    ')

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break
    else:
        print(n,'is a prime number')



