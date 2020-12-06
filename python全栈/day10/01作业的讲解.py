#写一个函数，此函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过循环输入这四个内容，然后将这四个内容传入函数中，此函数
#接收到这四个内容，将内容追加到一个student文件中，输入Q或q退出，性别默认为男，如果遇到女生，则把女生输入女。
def register(name, age, enducation, sex='男'):
    with open('student_msg', mode='a', encoding='utf-8') as f1:
        f1.write(f'{name}|{age}|{enducation}|{sex}\n')
        return


while 1:
    name = input('请输入姓名(Q或q退出)：')
    if name.lower() == 'q': break
    age = input('请输入年龄：')
    enducation = input('请输入学历：')
    sex = input('请输入性别(默认为男)：')
    if sex == '女':
        register(name, age, enducation, sex)
    else:
        register(name, age, enducation)
