#单分支结构
if True:
    print('条件正确')



#二分支结构
guees = eval(input('请输入你猜测的数字'))
if guees == 66:
    print('猜对了')
else:
    print('猜错了')


#多分支结构
guess = eval(input('请输入一个整数'))
if guess == 6:
    print('条件正确才执行')
elif guess > 6:
    print('只有满足elif的判断条件时才执行')
else:
    print('以上都不满足时，才执行else判断输出')


#异常处理
try:
    num = eval(input('请输入一个整数: '))
    print(num**3)
except NameError:
    print('请输入正整数')
#bmi指数的测量
height,weight = eval(input('请输入身高（米）和体重（公斤）【逗号隔开】：'))
bmi = weight / pow(height,2)
print('BMI数值为：{:.2f}'.format(bmi))
who,nat = '',''
if bmi < 18.5:
    who,nat = '偏瘦','便瘦'
elif 18.5 <= bmi < 24:
    who,nat = '正常','正常'
elif 24 <= bmi < 25:
    who,nat = '正常','偏胖'
elif 25 <= bmi <28:
    who,nat = '偏胖','偏胖'
elif 28 <= bmi <30:
    who,nat = '偏胖','肥胖'
else:
    who,nat = '肥胖','肥胖'
print('BMI指标为：国际"{0}",国内"{1}"'.format(who,nat))


