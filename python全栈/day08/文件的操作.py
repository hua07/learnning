#一、初识文件的操作。
#格式：f = （文件路径 ，编码方式，操作模式）
# 'F:/markdown/小米屏蔽网址.txt'#（你想操作一个文件必须知道文件位置）
# encoding = 'utf-8'（你需要知道这个文件是以什么编码储存的）
#mode = 'r'(操作模式：只读'r'，只写'w'，追加'a')
# f = open('f:\联系方式.txt', encoding='utf-8', mode='r')
# file = f.read()
# print(file)
# f.close()
""" 
opeen 内置函数，open底层调用的是操作系统的接口。
f 是一个变量，文件句柄。通过对文件进行的任何操作，都得通过文件句柄。
encoding:可以不写，不写参数，默认编码本：操作系统的默认的编码：windows是gbk，linux:utf-8,mac:utf-8
f.close()关闭文件句柄
"""

#文件操作的读：***
# f = open('f:\联系方式.txt', encoding='utf-8')
# content = f.read()
# print(content)
# f.close()

# 按照字符读取
# f = open('f:\联系方式.txt', encoding='utf-8')
# content = f.read(2)
# print(content)
# f.close()

#按照文件的行进行读
# f = open('f:\联系方式.txt', mode='r', encoding='utf-8')
# content = f.readline()
# print(content)
# f.close()

# readlines()返回一个列表，列表中的每个元素是源文件的每一行。 ***
# f = open('f:\联系方式.txt', mode='r', encoding='utf-8')
# content = f.readlines()
# print(content)
# f.close()

# for循环读取 ***
# f = open('f:\联系方式.txt', mode='r', encoding='utf-8')
# for i in f:
#     print(i)
# f.close()

#rb读取非本类文件，比如：图片，视频，音频
# f = open(r'C:\Users\king\Desktop\卡卡西.png', mode='rb')
# content = f.read()
# print(content)
# f.close()

#相对路径下的图片的读
# f = open('卡卡西.png', mode='rb')
# content = f.read()
# print(content)
# f.close()

#文件的写
# f = open('文件的写',encoding = 'utf-8',mode = 'w')
# f.write('随便写一些内容')
# f.close()

# f = open('文件的写', encoding='utf-8', mode='w')
# f.write('先清空原来的内容，再写入现在的内容')
# f.close()

#wb
# f = open('卡卡西.png', mode='rb')
# content = f.read()
# # print(content)
# f.close()
# f1 = open('卡卡西2.png',mode='wb')
# f1.write(content)
# f1.close()

#a 文件的追加
# f = open('文件的追加',encoding = 'utf-8',mode = 'a')
# f.write('king最帅')
# f.close()

# f1 = open('文件的追加',encoding = 'utf-8',mode = 'a')
# f1.write('大壮，舒淇，雪飞，b哥')
# f1.close()

#r+ 先读后写，
# f = open('文件的读写',encoding ='utf-8',mode='r+')
# content = f.read()
# print(content)
# f.write('人的一切的痛苦，本质都是对自己无能的愤怒。')
# f.close()

#文件的其他功能
#tell 获取光标的位置，单位字节
# f = open('文件的读写', encoding='utf-8')
# print(f.tell())
# content = f.read()
# print(f.tell())
# f.close()

#seek 调整光标位置
# f = open('文件的读写', encoding='utf-8')
# f.seek(9)
# content = f.read()
# print(content)
# f.close()

#flush 强制刷新
# f = open('文件的其他功能', encoding='utf-8', mode='w')
# f.write('这个是讲解文件的强制刷新保存')
# f.flush()
# f.close()

#打开文件的另一种方式
#优点1：不用手动关闭文件句柄
# with open('文件的读写',encoding='utf-8') as f1:
#     print(f1.read())

#优点2：
# with open('文件的读写',encoding= 'utf-8')as f1,\
#     open('文件的写',encoding ='utf-8',mode = 'w') as f2:
#         print(f1.read())
#         f2.write('这是新追加内容')

#文件的改的操作：实际上文件不存在该的操作，都是文件先读取，然后清空，再写入新的内容，最后重命名为原来文件名。
# import os
# with open('alex.txt',encoding='utf-8',mode='r') as f1,\
#     open('alex.txt.bak',encoding='utf-8',mode='w') as f2:
#     content = f1.read()
#     new_content = content.replace('alex', 'ALEX')
#     f2.write(new_content)
# os.remove('alex.txt')
# os.rename('alex.txt.bak', 'alex.txt')

#以上题举例，如果文件比较大就需要使用for循环来操作这个文件
# import os
# with open('alex.txt',encoding = 'utf-8',mode = 'r') as f1,\
#     open('alex.txt.bak',encoding = 'utf-8',mode = 'w') as f2:
#     for line in f1:
#         new_line = line.replace('ALEX', 'taibai')
#         f2.write(new_line)
# os.remove('alex.txt')
# os.rename('alex.txt.bak', 'alex.txt')
