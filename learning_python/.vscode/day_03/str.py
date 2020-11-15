""" value = 'alax'
new_value = value.upper()
print(new_value)
old_value = value.lower()
print(old_value) """
# 验证码的示例
""" 
cod = input('请输入验证码 iyUf')
if cod == 'iyUf':
    print('输入成功') 
"""
#  字符串大小写的转换 upper/lower
""" 第一个示例
code = 'uiYe'
cod = input('请输入验证码%s:'% code)
if cod.lower() == code.lower():
    print('验证成功')
if cod.upper() == code.upper():
    print('验证成功')
else:
    print('输入错误，请重新输入') 
"""
#第二个示例
value = 'alax'
new_value = value.upper()
print(new_value)

# isdigit 检查字符串是否只有数字组成，返回值为 Ture or false
""" 
while True:
    flage = input('输入你的学号：')
    date = flage.isdigit()
    if date == True:
        print('输入正确')
        break
    else:
        print('输入错误，请输入数字')
 """
# 去除空白 strip()/rstrip()/lstrip()
""" vlave = input('请输入你的昵称：')
new_name = vlave.strip()
print('-->',new_name,'<--') """
# 分隔字符串  split
""" sentence = input('请输入你想说的话：')
new_sentence = sentence.split('，',1)
print(new_sentence) """
# 替换字符 replace
""" name = input('请输入你的名字：')
print (name.replace('大爷','**'))
 """
# #############练习题##########
#让用户任意输入字符串，计算其中有多少个数字

