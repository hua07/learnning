li = [1,3,4,'alex',[3,7,8,'TaiBai'],5,'RiTiAn']
#循环打印列表中的所有元素，遇到小列表再循环打印它里面的元素。
for i in li:
    if type(i) != list:
        print(i)
    else:
        for m in i:
            print(m)
