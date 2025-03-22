def smart_divide(func):
    def inner(a,b):
        print("division of",a," and ",b )
        if b==0:
            print("cannot divide by ",b)
        func(a,b)
    return inner

def divide(a,b):
    print(a/b)

result = smart_divide(divide)
result(4,7)


