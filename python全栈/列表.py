# li = [100, '太白', '[1,2,3],True']
# #索引
# print(li[0], type(li[0]))
# print(li[1], type(li[1]))
# print(li[-1])

#练习题
# li = [1, 3, 2, 'a', 4, 'b', 5, 'c']
""" 
通过对li列表切片形成新的列表l1，l1 = [1,3,2]
通过对li列表切片形成新的列表l2, l2 = ['a',4,'b']
通过对li列表切片形成新的列表l3, l3 = [3,'a','b']
通过对li列表切片形成新的列表l4, l4 = ['b','a',3] """
# l1 = li[:3]
# l2 = li[3:6]
# l3 = li[1:-2:2]
# l4 = li[-3:0:-2]
# print(l1, l2, l3, l4)

#列表的创建
#方式一 l1 = list()
#方式二 l1 = list('adfwerasdfa')
#练习题：
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
""" 
计算列表的长度并输出
列表中追加元素"seven",并输出添加后的列表
请在列表的第1个位置插入元素"Tony",并输出添加后的列表
请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
请删除列表中的元素"ritian",并输出添加后的列表
请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
请删除列表中的第2至4个元素，并输出删除元素后的列表 """
# count = len(li)
# print(count)
# li.append('sever')
# print(li)
# li.insert(0,'Tony')
# print(li)
# li[1] = 'kelly'
# print(li)
# l2=[1,"a",3,4,"heart"]
# li.extend(l2)
# print(li)
# s = "qwert"
# li.extend(s)
# print(li)
# li.remove('ritian')
# print(li)
# word = li.pop(2)
# print(word,li)
# del li[1:4]
# print(li)

#列表的嵌套练习题
# l1 = [1, 2, 'taibai', [
#     1,
#     'alex',
#     3,
# ]]
""" 
1, 将l1中的'taibai'变成大写并放回原处。
2，给小列表[1,'alex',3,]追加一个元素,'老男孩教育'。
3，将列表中的'alex'通过字符串拼接的方式在列表中变成'alexsb'
 """
# l1[2] = l1[2].upper()
# l1[-1].append('老男孩教育')
# l1[-1][1] += 'sb'
# print(l1)

# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# 将列表lis中的"tt"变成大写（用两种方式）。
# lis[3][2][1][0] = lis[3][2][1][0].upper()
# lis[3][2][1][0] = 'TT'

# 将列表中的数字3变成字符串"100"（用两种方式）。
# lis[1] = 100
# lis[1] += 97
# 将列表中的字符串"1"变成数字101（用两种方式）。
# lis[3][2][1][-1] = 101
# lis[3][2][1][-1] = int(lis[3][2][1][-1]+'01')
# print(lis)

#range 类似与列表的一个自制数字范围的列表。
# r = range(10)
# print(r)
# for i in r:
#     print(i)
#range同样可以使用索引切片（步长）
# range多与for循环结合
# l1 =[1,2,3,'alex','太白']
#利用for循环和range将l1列表的所有索引打印出来
# for i in range(len(l1)):
#     print(i)
# l = [1, 2, 'a']
# l.extend('wang')
# print(l)
# l = [1, 2, 'a']
# l.insert(1, 'name')
# print(l)
#做一个简单的计算器的交互，让用户输入如5+9，5 +9 5 + 9 然后计算他的和 ，差，积，商
""" 
content = input('请输入内容：')
li_content = content.split('+')
sum = 0
for i in li_content:
    sum += int(i.strip())
print(sum) """

# li = ['TaiBai','alexC','AbC','egon','riTiAn','WuSir','aqc']
# #查找列表li中的元素，移除每个元素的空格，并找出以A或a开头，并以c结尾的所有元素，并把他们添加到一个新的列表中，
# #最后循环打印这个新的列表
# new_li = []
# for word in li:
#     if word.strip().startswith('a'or'A') and word.strip().endswith('c'):
#         new_li.append(word.strip())
# print(new_li)

#开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的包含特殊字符：
#敏感词列表li中，则将用户输入的内容中的敏感词汇替换成等长度的*，并添加到一个列表中，如果用户输入的没有
#敏感词汇，就直接添加到新的列表中
""" 
li = [
    '苍老师',
    '东京热',
    '武腾兰',
    '波多野结衣',
]
word = input('请输入评论内容：')
new_li = []

for i in li:
    if i in word:
        word = word.replace(i, len(i) * '*')
new_li.append(word)
print(new_li) """

li = [1, 3, 4, 'alex', [3, 7, 8, 'TaiBai'], 5, 'RiTiAn']
#循环打印列表中的所有元素，遇到小列表再循环打印它里面的元素。
for i in li:
    if type(i) != list:
        print(i)
    else:
        for m in i:
            print(m)
