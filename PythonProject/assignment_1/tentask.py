try:
    x = int(input("enter a number1 : "))
    y = int(input("enter a number2 : "))
except ValueError:
    raise TypeError("type error")