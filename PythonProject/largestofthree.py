a = int(input("enter the number 1: "))
b = int(input("enter the number 2: "))
c = int(input("enter the number 3: "))

if a>b:
    temp=a
else:
    temp=b

if c>temp:
    temp = c
print("largest number among three is", temp)