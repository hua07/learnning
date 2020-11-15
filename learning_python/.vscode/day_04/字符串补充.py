#1startswith/endswith
""" name = 'wangjinhua'
flag = name.startswith('waa')
print(flag) """
#2字符串格式化 format
""" name = '我叫{0}，今年{1}'.format('lining',72)
print(name) """
#3.encode 字符串编码的转换
""" name = '王朋'
v1 = name.encode('UTF-8')
v2 = name.encode('GBK')
print(v1,v2) """
#4.join 拼接
""" name = 'alax'
result = '_'.join(name)#循环每个元素，并在元素之间加入连接符。
print(result) """
