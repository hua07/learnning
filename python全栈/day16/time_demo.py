""" 
time 模块
"""
import time
#获取时间戳
#时间戳：从时间元年(1970 1 1 00：00：00)到现在经过的秒数。
print(time.time())  #1608709596.5051181

#获取格式化时间对象
# 默认参数是当前系统时间的时间戳
print(time.gmtime())
print(time.localtime())

#格式化时间对象和字符串之间的转换
s = time.strftime('year:%Y %m %d %H:%M:%S')
print(s)
#把时间字符串转换成时间对象

#time.sleep()
for i in range(5):
    print(time.strftime('%Y %m %d %H:%M:%S'))
    #让程序睡1秒
    time.sleep(1)

#date 类：
