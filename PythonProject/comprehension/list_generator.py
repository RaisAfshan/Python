list1 = [1,2,3,4,5,6,7,9]
list2 = (i for i in list1 if i%2 ==0)
for var in list2:
    print(var,end=" ")