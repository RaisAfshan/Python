n = 10
num1 = 0
num2 = 1
next_no = num2
count = 1
print(num1,num2,"" ,end="")
while count <= n:
    print(next_no, end=" ")
    count += 1
    num1 = num2
    num2 = next_no
    next_no = num1 + num2
print()