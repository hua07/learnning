a = 1
def fun_1():   
    a = 2   
    def fun_2():       
        nonlocal a       
        a = 3       
        def fun_3():           
            a = 4           
            print(a)  # 4     
        print(a)  # 3     
        fun_3()       
        print(a)   # 3
    print(a)  # 2
    fun_2()   
    print(a) # 3
print(a) # 1
fun_1() 
print(a) # 1