num1 = int(input("enter the number 1 : "))
num2 = int(input("enter the number 2 : "))
num3 = int(input("enter the number 3  : "))

if(num1<num2):
    temp=num1
else:
    temp=num2
if(num3<temp):
    temp=num3

print("smallest number : " , temp)
