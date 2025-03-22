#positional args
def func(a,b):
    print(a,b)

func(3,4)

#keyword args
def func2(a,b):
    print("keyword args ----> ",a,b)

func2(b=4,a=7)

# default args
def func3(a,b=0):
    print("default ---->" , a, b )

func3(12)

#aribiyaury positional args
def func4(a,b,*args):
    print("aribiyaurt positional args ---->",a,b,args);

func4(1,2,34,45,6,67,8)

#aribitaury keywords args
def func5(a,b,**args):
    print("aribitaury keywords args ----> ",a,b,args);

func5(a=2,b=3,args=(23,5,67,3,45))