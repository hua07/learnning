#初级难度：设计一个重量转换器，输入以'g'为单位代数字后返回换算成'kg'的结果
def conversion(k):
    weight = k/1000
    return weight
s = 7
new_s = conversion(s)
print(f's的重量单位换算成kg是{new_s}kg')