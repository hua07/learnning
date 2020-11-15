

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
# 这个外星人的速度一定很快
    x_increment = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

#由类似对象组成的字典
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'eathon':'ruby',
    'phil':'python',
    }
for i in favorite_languages:
    print(favorite_languages[i].title(),end = ',')



# 6-1使用一个字典来存储一个熟人的信息，包括名、姓、年龄、和居住的城市。该字典应包含
# 键first_name、last_name、age和city。将存储在该字典中的每项信息都打印出来。

personal_information = {
    'first_name':'libai',
    'last_name':'shixian',
    'age':'180',
    'city':'songchao'}
print(personal_information['first_name'])
print(personal_information['last_name'])
print(personal_information['age'])
print(personal_information['city'])

 


# 6-2 喜欢的数字：使用一个字典存储一些人喜欢的数字。请想出5个人的名字，并将这些名字
# 用作字典中的键；想出每个人喜欢的一个数字，存储到字典中，打印字典的所有项。
luck_number = {}
luck_number['zhengke']='6'
luck_number['guaiwan']='7'
luck_number['keke']='8'
luck_number['doudou']='9'
luck_number['kun']='0'
print(luck_number)
print('zhengke'+'的幸运数字是'+luck_number['zhengke'])
print('guaiwan'+'的幸运数字是'+luck_number['guaiwan'])
print('keke'+'的幸运数字是'+luck_number['keke'])
print('doudou'+'的幸运数字是'+luck_number['doudou'])
print('kun'+'的幸运数字是'+luck_number['kun'])



# 6-3词汇表：python字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者称为词汇表。
words = {}
words['title（）']='首字母大写的方法'
words['upper()']='全大写输出的方法'
words['lower()']='全小写输出的方法'
words['float']='提取中间值函数'
words['del']='删除语句'
words['remove()']='删除方法'
for i ,v in words.items():
    print(i+':'+v)





"""
6-4 词汇表2 ：既然你知道了如何遍历字典，现在请整理你为完成练习6-3而编写的代码，
将其中的一系列print 语句替换为一个遍历字典中的键和值的循环。确定该
循环正确无误后，再在词汇表中添加5个Python术语。当你再次运行这个程序时，
这些新术语及其含义将自动包含在输出中。
 """
python_dictionary = {
    'title':'首字母大写',
    'upper':'全大写',
    'lower':'全小写',
    'len':'计数',
    'float':'转换成浮点数',
    }
python_dictionary['int'] = '转换成数字'
python_dictionary['str'] = '转换成字符串'
python_dictionary['strip'] = '移除字头字尾的空格'
python_dictionary['append'] = '末尾插入'
python_dictionary['insert'] = '插入'
python_dictionary['del'] = '永久删除'

for word in python_dictionary.keys():
    print('\n'+word,'i know how to use ')
for word in python_dictionary.keys():
    print('\n',word)
for use in python_dictionary.values():
    print('\n',use)
name = ['str','pop','remove','range','sort']
for t in name:
    if t in python_dictionary.keys():
        print('\n'+t,'谢谢你的参与')
    else:
        print('\n'+t,'邀请你来加入我们')




# 6-5 河流：创建一个字典，在其中存储三条河流及其流经的国家。其中一个键值对可能是'nile'
# :'egypt'
rivers = {
    'nile':'坦桑尼亚',
    'Amazon':'巴西',
    'changjiang':'中国'
    }
for river,country in rivers.items():
    print('The'+river.title()+'runs through'+country.title())
    print(river.title())
    print(country.title())
for name in rivers.keys():
    print(name)
for i in rivers.values():
    print(i)


# 6-6 调查：在favorite_languager.py中执行以下操作。
# 创建一个应该会接受调查的人员名单，其中有些人已经包含在字典中，而其他人未包含在字典中。
# 遍历这个人员名单，对于已参加调查的人员，打印一条消息表示感谢。对于还未参加的邀请参加。
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'eathon':'ruby',
    'phil':'python',
    }
names = ['jen','eathon','kebi','joden']
for name in names:
    if name in favorite_languages.keys():
        print(name+'感谢您的参与')
    else:
        print(name+'您还没有接受调研，欢迎你来参与')



# 创建一个外形人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speen':'slow'}
    aliens.append(new_alien)
# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print('...')
# 显示创建了多少个外星人
print('total number of aliens:'+str(len(aliens)))


"""6-7 人 ：在为完成练习6-1而编写的程序中，再创建两个表示人的字典，
然后将这三个字典都存储在一个名为people 的列表中。遍历这个列表，将其中每个人的所有
信息都打印出来。

 """
peoples = []
people = {
    'first_name':'libai',
    'last_name':'shixian',
    'age':'180',
    'city':'songchao',
    }
peoples.append(people)
people = {
    'first_name':'dufu',
    'last_name':'shisheng',
    'age':'190',
    'city':'tangcao',
    }
peoples.append(people)
people = {
    'first_name':'menghaoran',
    'last_name':'shiren',
    'age':'110',
    'city':'tangcao',
}
peoples.append(people)
for people in peoples:
    name = people['first_name']+people['last_name']
    age = people['age']
    city = people['city']
    print(name+':'+age+city)



# 6-8 宠物：创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；在每个字典中，
# 包含类型及其主人的名字。将这些字典存储在一个名为pets的列表中，遍历列表打印所有信息。
pets = []
pet = {
    'name':'cat',
    'master':'xiaoming',
    'type':'bosimao',
}
pets.append(pet)
pet = {
    'name':'dog',
    'master':'lilei',
    'type':'hashiqi',
}
pets.append(pet)
pet = {
    'name':'bird',
    'master':'xiaohua',
    'type':'yingwu',
}
pets.append(pet)

for pet in pets:
    name = pet['name']
    master = pet['master']
    leixing = pet['type']
    print(name+':\n\t'+'master:'+master+'\ttype:'+leixing)


# 6-9 喜欢的地方：创建一个名为favorite_places的字典，用三个人的名字用作键，对每个人
# 都存储1-3个喜欢的地名。遍历字典，打印每个人的名字及其喜欢的地方、
favorite_places = {
    'libai':['hangzhou','suzhou','shanghai'],
    'dufu':['guangzhou','yunnan'],
    'baijuyi':['jiangsu'],
}
for key,value in favorite_places.items():
    print('\n'+key+'喜欢的地方有以下：')
    for place in value:
        print(place,end = '     ')


# 6-10 喜欢的数字：修改6-2的练习程序，让每个人有多个喜欢的数字，然后打印出来。
luck_number = {
    'zhegnke':[6,8,9,0],
    'keke':[1,3,5],
    'guaiwan':[1,5,7.3]
}
for key,values in luck_number.items():
    print('\n'+key+'喜欢的数字有：')
    for number in values:
        print(number,end='、')



# 6-11 城市：创建一个名为cities的字典，其中将三个城市名用作键；对于每座城市，都创建
# 一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。在表示每座
# 城市的名字以及有关它们的信息都打印出来。
cities = {
    'shanghai' : {
    'country':'chana',
    'populace':'280000',
    'fact':'中国的魔都',},

    'london' :{
    'country':'england',
    'populace':'1000000',
    'fact':'英国的雾都',},

    'tykyo' :{
    'country':'japan',
    'populace':'50000',
    'fact':'日本的首府',},
}
for city ,information in cities.items():
    country = information['country']
    populace = information['populace']
    fact = information['fact']
    print(city+':\n'+'所属的国家是：'+country.title()+",常驻的人口有："+populace.title()+
    '是'+fact)




