print('from the tb_dome.py')
name = '太白金星'


def read1():
    print('tb_dome模块：', name)


def read2():
    print('tb_dome模块')
    read1()


def change():
    global name
    name = 'barry'
