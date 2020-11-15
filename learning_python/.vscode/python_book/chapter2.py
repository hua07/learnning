#字符串
#使用方法修改字符串的大小写
# example01 :
name = 'my king'
print(name.title())
print(name.upper())，
print(name.lower())

""" 在这个示例中，小写的字符串"my king" 存储到了变量name 中。在print() 语句中，方法title() 出现在这个变量的后面。
方法 是Python可对数据执行的操作。在name.title() 中，name 后面的句点（. ）让Python对变量name 执行方法title() 指定
的操作。每个方法后面都跟着一对括号，这是因为方法通常需要额外的信息来完成其工作。这种信息是在括号内提供的。函数title()
 不需要额外的信息，因此它后面的括号是空的。
 """
language = str(input('请输入你喜欢的编程语言：'))
print(language)
print(language.title())
print(language.lower())
print(language.upper())
print(language.strip())
