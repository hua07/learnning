#随机生成函数random
import random

print (random.random())
print (random.random())

print ("------- 设置种子 seed -------" , random.seed( 10 ))
print ("Random number with seed 10 : ", random.random())

# 生成同一个随机数
random.seed( 10 )
print ("Random number with seed 10 : ", random.random())

# 生成同一个随机数
random.seed( 10 )
print ("Random number with seed 10 : ", random.random())

