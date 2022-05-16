# 自己的列表：罗列出自己的出行方式，并对每个出行方式制定一句宣言，根据列表打印宣言。
ways = ['bicycle', 'bus', 'subway', 'tram', 'car']
for i in ways:
    if i in ways[0]:
        print('{}'.format(ways[0]), ':是最慢的方式，但是可以锻炼身体')
    elif i in ways[1]:
        print('{}'.format(ways[1]), ':最不喜欢的出行方式，但是有时候不得不。')
    elif i in ways[2]:
        print('{}'.format(ways[2]), ':比较快速，就是到家的距离有点远。')
    elif i in ways[3]:
        print('{}'.format(ways[3]), ':很喜欢的一种出行方式，但是天气坏的时候无法使用。')
    else:
        print('{}'.format(ways[4]), ':额，暂时还没有自己汽车，比较遗憾。')
"""
学会使用
title,upper,lower,sprit,insert,del,pop,remove,

 """

friends = ['zhengke', 'keke', 'guaiwan', 'doudou', 'jiji', 'segun', 'banzhang']
# jiji 无法参加聚会，但是xiaoshizi可以来
friends[4] = 'xiaoshizi'
#还想邀请两位女士，分别添加到列表的开始和末尾
friends.insert(0, 'yuehua')
friends.append('gcyryr')
for i in range(len(friends) - 2):
    friend = friends.pop()
    print('sorry', friend + '由于位置有限，不能和你共进晚餐了')
print('{}我们依旧可以共进晚餐'.format(friends[0]))
print('{}我们依旧可以共进晚餐'.format(friends[1]))
print(friends)
del friends[0]
del friends[0]
print(friends)
""" 
本次目标学会使用：sort（）按照字母顺序永久性排序列表
sorted（）：暂时性排序列表
reverse（）：修改列表元素的排列顺序
使用

 """
""" 
放眼世界 ：想出至少5个你渴望去旅游的地方。
将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python列表。
使用sorted() 按字母顺序打印这个列表，同时不要修改它。
再次打印该列表，核实排列顺序未变。
使用sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它。
再次打印该列表，核实排列顺序未变。
使用reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
使用reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
使用sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
使用sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
 """
cities = ['beijing', 'shanghai', 'zhengzhou', 'hangzhou', 'xianggang', 'aomen']
print(cities)
cities.sort()
print(cities)
cities.reverse()
print(cities)
print(sorted(cities))

# 3-1 姓名： 姓名： 将一些朋友的姓名存储在一个列表中，并将其命名为names 。依次访问该列表中的每个元素，
# 从而将每个朋友的姓名都打印出来。
names = ['zhengke', 'keke', 'guaiwan', 'doudou']
for i in names:
    print(i.title())

# 3-2 问候语： 问候语： 继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。
# 每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
names = ['zhengke', 'keke', 'guaiwan', 'doudou']
for i in names:
    print(i.title(), '最近怎么样啊。')

# 3-3 自己的列表： 自己的列表： 想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。
# 根据该列表打印一系列有关这些通勤方式的宣言，如“I would like to own a Honda motorcycle”。
transportation = ['bike', 'car', 'train', 'bus', 'tram']
for i in transportation:
    print('我最喜欢的通勤方式是：', i.title())

# 3-4 嘉宾名单：如果你可以邀请一些人一起共进晚餐，你会邀请那些人？创建一个列表。然后使用这个列表打印消息，邀请他们
# 共进晚餐
names = ['zheng ke', 'ke ke', 'guai wan', 'dou dou']
massege = '晚上一起吃饭吧。'
print(names[0].title() + '\n\t' + massege)
print(names[1].title() + '\n\t' + massege)
print(names[2].title() + '\n\t' + massege)
print(names[3].title() + '\n\t' + massege)

#3-5 修改嘉宾名单：用print语句指出一位嘉宾无法来了，邀请一位新的嘉宾替换无法来的那位。再次打印邀请信息。
names = ['zheng ke', 'ke ke', 'guai wan', 'dou dou']
massege = '晚上一起吃饭吧。'
print(names[3].title(), '由于突发事件无法来参加晚餐了')
names[3] = 'ya kun'
print(names[0].title() + '\n\t' + massege)
print(names[1].title() + '\n\t' + massege)
print(names[2].title() + '\n\t' + massege)
print(names[3].title() + '\n\t' + massege)

#3-6 再次添加3个嘉宾。用print语句指出找到了更大餐桌。使用insert（）将一位嘉宾添加到名单开头。
#一位添加到中间，使用append（）将一位添加到末尾。打印邀请信息。
names = ['zheng ke', 'ke ke', 'guai wan', 'dou dou']
massege = '晚上一起吃饭吧。'
print('现在有更大的餐桌了，可以再多邀请3位嘉宾来共进晚餐')
names.insert(0, 'yakun')
names.insert(3, 'ji ji')
names.append('xiao shi zi')

print(names[0].title() + '\n\t' + massege)
print(names[1].title() + '\n\t' + massege)
print(names[2].title() + '\n\t' + massege)
print(names[3].title() + '\n\t' + massege)
print(names[4].title() + '\n\t' + massege)
print(names[5].title() + '\n\t' + massege)
print(names[6].title() + '\n\t' + massege)

#3-7 缩减名单：现在餐桌没有位置了，你只能要求两位来共进晚餐。打印一条你只能邀请两位的嘉宾共进晚餐。
#使用pop（）不断的删除名单中的嘉宾，直到只有两位嘉宾为止，每次从名单中弹出一位嘉宾时，都打印一条信息，让嘉宾
#知悉你很抱歉，对余下的两位嘉宾都打印一条消息，指出他们依然在首邀之列。使用del将最后的两位嘉宾从名单中删除，
#让名单变成空的，打印该名单，合适程序结束时名单确实是空的。

names = ['zheng ke', 'ke ke', 'guai wan', 'dou dou']
massege = '晚上一起吃饭吧。'
print('现在有更大的餐桌了，可以再多邀请3位嘉宾来共进晚餐')
names.insert(0, 'ya kun')
names.insert(3, 'ji ji')
names.append('xiao shi zi')
new_massege = '很不幸，刚接到通知现在已经没有餐桌了，无法邀请那么多人来参加晚餐。只能邀请两位，抱歉了'
first_one = names.pop(0)
print(first_one.title() + new_massege)
second_one = names.pop(2)
print(second_one.title() + new_massege)
third_one = names.pop(-1)
print(third_one.title() + new_massege)
fourthly_one = names.pop(-2)
print(fourthly_one.title() + new_massege)
fifthly_one = names.pop(-1)
print(fifthly_one.title() + new_massege)
print(names[0].title() + massege)
print(names[1].title() + massege)
del names[0]
del names[0]
print(names)

#3-8 放眼世界：想出至少5个你想去的地方，1、将这些地方储存到列表中，并确保不是按照字母顺序排列的
#2、按原始顺序打印列表，3、使用sorted（）打印该列表同时不要修改它。4、再次打印该列表，核实列表顺序未变。
#5、使用sorted（）按字母顺序相反的顺序打印这个列表，同时不要修改它。6、再次打印该列表
#7、使用reverse()修改列表元素的排列顺序，打印核实列表确实改变了。8、使用reverse（）再次打印，核实已恢复到原来排列顺序。
#8、使用sort（）修改该列表，使其元素安字母顺序排列。打印该列表，核实排列顺序确实变了。9、再次使用sort（）修改列表，核实是否改变。

cities = ['xi zang', 'tai wan', 'gui lin', 'da li', 'ri ben']
print(cities)
print(sorted(cities))
print(sorted(cities, reverse=True))
cities.reverse()
print(cities)
cities.reverse()
print(cities)
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)
