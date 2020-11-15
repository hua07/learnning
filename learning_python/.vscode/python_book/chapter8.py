# 本章节主要内容：学习编写函数
# 2019，12，30

# 示例：显示简单的问候语
def greet_user(user_name):
    """ 显示简单的问候语 """
    print('hello,'+user_name.title()+'!')
greet_user('xiaoming')



# 8-1 消息：编写一个名为display_message()的函数，它打印一个句子，指出你在本章学的是
# 什么。调用这个函数，确认显示的消息正确无误。
def display_message():
    """ 打印一个句子，指出本章学习内容 """
    print('本章主要学习的是编写函数')
display_message()



# 8-2 喜欢的图书：编写一个名为favorite_book()的函数，其中包含一个名为title的形参。
# 这个函数打印一条消息。如one of ma favorite books is alice inwonderland.
# 调用这个函数，并将一本图书的名称作为实参传递给它。
def favorite_book(title):
    print('one of ma favorite books is '+ title.title()+' inwonderland')
favorite_book('newbook')
