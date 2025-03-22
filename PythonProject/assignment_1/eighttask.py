def countdown(x):
    if(x>=5):
        while x>=5:
            print(x)
            x=x-1
    else:
        while x<=5:
            print(x)
            x=x+1

x = int(input("enter the number"))
countdown(x);



