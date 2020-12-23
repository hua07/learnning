#如果没有len（）函数了现在让你统计一个对象的元素个数：
s1 = 'adsfjklwejrlkjasdguio'
count = 0
for i in s1:
    count += 1
print(count)


#如果你在一个编程文件中多次使用计数，每次都需要重新编一编。所以有一个方法，就是定义一个函数，在需要计数时随时调用。
def new_len(Iterative):
    count = 0
    for i in Iterative:
        count += 1
    return count


s2 = 'adfwertkjglm'
print(new_len(s2))

#函数：以功能为导向，一个函数就是一个功能。随调随用，
#减少代码的重复性。
#增强了代码的可读性。

# return：
# 1、在代码中是终止函数，返回一个指定对象，
# 2、如果eturn返回多个元素时，是以元组的形式返回给函数的执行者


#初级难度：设计一个重量转换器，输入以'g'为单位代数字后返回换算成'kg'的结果
def conversion(k):
    weight = k / 1000
    return weight


s = 7
new_s = conversion(s)
print(f's的重量单位换算成kg是{new_s}kg')


#中级难度：设计一个求指教三角形斜边长的函数（两条指教边为参数，求最长边如果指教边边长分别为3和4，那么返回的结果为：5
def trigon_bevelling(a, b):
    c = (a**2 + b**2)**0.5
    return c


a = 3
b = 4
c = trigon_bevelling(a, b)
print(f'这个直角三角形的斜边长为{c}')

#第二种方法：
c = lambda a, b: (a**2 + b**2)**0.5
a = 3
b = 4
x = c(a, b)
print(f'这个直角三角形的斜边长为{x}')