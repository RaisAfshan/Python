

try:
    a = int(input("enter the number 1  : "))
    b = int(input("enter the number 2 : "))

    try:
        z=a/b
        print(z)
    # except ZeroDivisionError:
    #     print("zerodivisionzero")
    # except TypeError:
    #     print("type error")
    except Exception as e:
        print("the error is", e)

except:
    print("input error")