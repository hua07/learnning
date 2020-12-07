a = 10
b = 20


def test(a, b):
    print(b, a)


c = test(b, a)
print(c)  #没有返回值所以是None


def wrapper():
    def inner():
        print(666)

    inner()


wrapper()