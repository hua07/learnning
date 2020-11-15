""" 
5-3 外星人颜色#1 ：假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color 的
变量，并将其设置为'green' 、'yellow' 或'red' 。
编写一条if 语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了
5个点。
编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过
（未通过测试时没有输出）。
 """

alien_color = ['green','yellow','red']
for kelled in alien_color:
    if kelled == 'green':
        print('成功击杀，获得5点经验')

""" 
5-4 外星人颜色#2 ：像练习5-3那样设置外星人的颜色，并编写一个if-else 结构。
如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5个点。
如果外星人不是绿色的，就打印一条消息，指出玩家获得了10个点。
编写这个程序的两个版本，在一个版本中执行if 代码块，而在另一个版本中执行else 代码块。
 """
alien_color = ['green','yellow','red']
for kelled in alien_color:
    if kelled == 'green':
        print('成功击杀小兵，获得5点经验') 
    elif kelled != 'green':
        print('成功击杀精英怪，获得10点经验')

""" 
5-6 人生的不同阶段 ：设置变量age 的值，再编写一个if-elif-else 结构，
根据age 的值判断处于人生的哪个阶段。
如果一个人的年龄小于2岁，就打印一条消息，指出他是婴儿。
如果一个人的年龄为2（含）～4岁，就打印一条消息，指出他正蹒跚学步。
如果一个人的年龄为4（含）～13岁，就打印一条消息，指出他是儿童。
如果一个人的年龄为13（含）～20岁，就打印一条消息，指出他是青少年。
如果一个人的年龄为20（含）～65岁，就打印一条消息，指出他是成年人。
如果一个人的年龄超过65（含）岁，就打印一条消息，指出他是老年人。

 """
age = float(input('请输入年龄：'))
if age < 2:
    print('还是个婴儿')
elif age < 4:
    print('他正在蹒跚学步')
elif age < 13:
    print('这时儿童')
elif age < 20:
    print('这是青少年')
elif age < 65:
    print('他是成年人')
elif age > 65:
    print('他是老年人')    

""" 
5-7 喜欢的水果 ：创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if 语句，
检查列表中是否包含特定的水果。
将该列表命名为favorite_fruits ，并在其中包含三种水果。
编写5条if 语句，每条都检查某种水果是否包含在列表中，如果包含在列表中，
就打印一条消息，如“You really like bananas!”。
 """

fruits = ['apple','orange','banana','pear']
for i in fruits:
    if i == 'banana':
        print('i really like :'+i)
    else:
        print(i,'不是我的最爱')

""" 
5-10 检查用户名 ：按下面的说明编写一个程序，
模拟网站确保每位用户的用户名都独一无二的方式。
创建一个至少包含5个用户名的列表，并将其命名为current_users 。
再创建一个包含5个用户名的列表，将其命名为new_users ，
并确保其中有一两个用户名也包含在列表current_users 中。
遍历列表new_users ，对于其中的每个用户名，都检查它是否已被使用。
如果是这样，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指
出这个用户名未被使用。
确保比较时不区分大消息；换句话说，如果用户名'John' 已被使用，应拒绝用户名'JOHN' 。
"""

current_users = ['Xiaoming','Lilei','hanmeimei','xiaofang','xiaonan']
new_users = ['lilei','xiaoming','libai','dufu','wangxizhi']
for i in new_users:
    for l in current_users:
        if i.lower() == l.lower():
            print('昵称已被占用')
        print('该昵称可以使用')

#5-11序数表示位置，如1st、2nd。大多数序数都是以th结尾，除了1、2、3、例外。
#创建一个数字列表1-9，遍历这个列表，打印每个数字对应的序数。例如1st

numbers = range(1,10)
for i in numbers:
    if i == 1:
        print(str(i)+'st',end = '\n')
    elif i == 2:
        print(str(i)+'nd',end = '\n')
    elif i == 3:
        print(str(i)+'rd',end = '\n')
    else:
        print(str(i)+'th',end = '\n')



