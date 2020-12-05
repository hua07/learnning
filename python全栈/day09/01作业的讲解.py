#有如下文件，al.txt,里面的内容为：
# 老男孩是最好的学校，
# 全心全意为学生服务，
# 只为学生未来，不为牟利。
# 我说到都是真的。哈哈h

# 分别完成以下功能：
# 将原文件全部读出来并打印。
# with open('al.txt',encoding = 'utf-8',mode = 'r') as f1:
#     for i in f1:
#         print(i)
# 在原文件后面追加一行内容：信不信由你，反正我信了。
# with open('al.txt', encoding='utf-8', mode='a') as f2:
#     f2.write('\n信不信由你，反正我信了')

# 将原文件全部读出来，并在后面添加一行内容：信不信由你，反正我是信了。
# with open('al.txt',encoding = 'utf-8',mode = 'r+') as f3:
#     for i in f3:
#         print(i)
#     f3.write('\n信不信由你，反正我是信了')
# 将原文件却不清空，换成下面的内容：
import os
with open('al.txt',encoding = 'utf-8',mode = 'r') as f1,\
    open('a2.txt',encoding = 'utf-8',mode = 'w') as f2:
    f2.write('每天坚持一点，\n每天努力一点，\n每天多思考一点，\n慢慢你会发现，\n你的进步越来越大。')
os.remove('al.txt')
os.rename('a2.txt', 'al.txt')
#每天坚持一点，
#每天努力一点，
#每天多思考一点，
#慢慢你会发现，
#你的进步越来越大。
