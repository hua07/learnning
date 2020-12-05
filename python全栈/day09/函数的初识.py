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
