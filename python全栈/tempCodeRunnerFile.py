word = 'hello,世界'
new_word = word.encode('gbk')
print(new_word)

#非unicode编码之间的转换
word1 = new_word.decode('gbk')
print(word1)
word2 = word1.encode('utf-8')
print(word2)