def decor(func):
    def inner(a,b):
        print("sum of",a ," and ",b)
        func(a,b)
    return inner

@decor
def sum(a,b):
    print(a+b)

sum(8,5)