#汽车租赁：询问客户要租赁什么样的汽车，并打印一条消息，如“let me see if i can find you subaru”。
""" 
car_name = input('请问你想租赁什么样的汽车？')
print('let me see if i can find you ' + car_name)
 """

#餐馆订位：编写一个程序，询问客户有多少人用餐。如果超过8人，就打印指出没有空桌；否则指出空桌。
person = input('请问你需要预定多少人的座位呢: ')
if int(person) > 8:
    print('不好意思，现在没有这么大的空桌了')
else:
    print('现在还有以下的空余桌位：88号桌' )

#10的整倍数：让用户输入数字，并指出这个数字是否是10的整数倍。
num = input('请输入10的整数倍： ')
if int(num) % 10 == 0:
    print('输入正确')
else:
    print('输入错误')
#7-4 比萨配料 ：编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit' 
# 时结束循环。每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添加这种配料。
while True:
    pizaa = input('请依次输入你想添加的比萨配料，最后以quit结束：')
    if pizaa == 'quit':
        break
    else:
        print('我们会添加' + pizaa+'这种配料')
        

#7-5 电影票 ：有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3~12岁的观众为10美元；
# 超过12岁的观众为15美元。请编写一个循环，在其中询问用户的年龄，并指出其票价。

age = int(input('请输入你的年龄： '))
while True:
    if age < 3:
        print('年龄小于3岁，观影免费')
    elif age > 12:
        print('请您支付15美元')
    else:
        print('请您支付10美元')
    break



# 7-8 创建一个名为sandwich_orders的列表，在其中包含各种三明治的名字；再创建一个名为
# finished_anwichesd 空列表。遍历列表sandwich_orders,对于其中的三明治都打印一条消息
# 如i made your tuna sandwich,并将其转移到列表finished_sandwiches。所有三明治都制作
# 好后，打印一条消息，将这些三明治列出来。
sandwich_orders = ['青椒','牛腩','土豆','辣椒']
finished_sanwichesd = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('i made your'+sandwich+'sandwich')
    finished_sanwichesd.append(sandwich)
for finished in finished_sanwichesd:
    print(finished)


# 7-9 五香烟熏牛肉（pastrami）卖完了：使用为完成练习7-8而创建的列表sandwich_orders,
# 并确保'pastrami'在其中至少出现三次。在程序开头附近添加这样的代码：打印一条消息，指出
# 熟食店的五香牛肉卖完了；再使用一个while循环将列表sandwich_orders中的'pastrami'都
# 删除。确认最终的列表finished_sandwiches中部包含'pastrami'。
sandwich_orders = ['青椒','牛腩','土豆','辣椒','pastrami','pastrami','pastrami',]
print('熟食店的pastrami卖完了')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
for sandwich in sandwich_orders:
    print(sandwich)