#索引的时候中括号里的数字第一个是起始位置，第二个数字是终止位置，
# 第三个位置是步长（告诉大家每次走几步）
""" name = 'niadjiausdif'
print(name[0:4:2]) """
#输出大写
""" name = 'alax'
new_name = name.upper()
new_name2 = name.lower()
print(new_name,new_name2) """
#验证码的练习
""" while True: 
    code = 'ALax'
    volue = input('请输入验证码%s:'%code)
    if code.upper() == volue.upper():
        print('登录成功')
        break
    else:
        print('输入错误，请重新输入')
"""

#检查是否是整型，isdigit返回的数据类型是bool值（True or False)
""" volue = '777'
new_volue = volue.isdigit()
print(new_volue) 
"""

