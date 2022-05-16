while True: 
    code = 'ALax'
    volue = input('请输入验证码%s:'%code)
    if code.upper() == volue.upper():
        print('登录成功')
        break
    else:
        print('输入错误，请重新输入')
