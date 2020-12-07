#%s  format  f''
name = 'king'
age = 18
msg = '我叫%s,今年%s' % (name, age)
msg1 = '我叫{},今年{}'.format(name, age)
msg2 = f'我叫{name},今年{age}'
print(msg, '\n', msg1, '\n', msg2)
