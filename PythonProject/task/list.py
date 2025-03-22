my_List = [1,2,3,4,5,6,7,8,9,10,11,12,13,24]
even = []
odd = []
for i in my_List:
    if(i % 2 == 0):
        print("this is even -->",i)
        even.append(i)
    else:
        print("this is odd -->",i)
        odd.append(i)

print("even -->",even)
print("odd -->",odd)
