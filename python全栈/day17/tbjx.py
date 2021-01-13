print('from the tbjx.py')
name = '太白金星'


def read1():
    print('tbjx模块：', name)


def read2():
    print('tbjx模块')
    read1()


def change():
    global name
    name = 'barry'


print(__name__)
#当脚本使用：__name__==__main__ 返回True
#当做模块被别人使用时：__name__==tbjx

#当模块需要调试时：if __name__==__main__ 需要使用这个判断条件
