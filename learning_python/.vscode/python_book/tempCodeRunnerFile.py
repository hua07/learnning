friends = ['zhengke','keke','guaiwan','doudou','jiji','segun','banzhang']
# jiji 无法参加聚会，但是xiaoshizi可以来
friends[4] = 'xiaoshizi'
#还想邀请两位女士，分别添加到列表的开始和末尾
friends.insert(0,'yuehua')
friends.append('gcyryr')
for i in range(len(friends)-2):
    friend = friends.pop()
    print('sorry',friend+'由于位置有限，不能和你共进晚餐了')
print('{}我们依旧可以共进晚餐'.format(friends[0]))
print('{}我们依旧可以共进晚餐'.format(friends[1]))
print(friends)
del friends[0]
del friends[0]
print(friends)