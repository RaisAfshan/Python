list1 = [10,20,25,30,35]
list2 = [40,45,60,75,90]

odd = list(filter(lambda x:x%2 != 0,list1))
even = list(filter(lambda x:x%2==0,list2))

print("even number --->",even)
print("odd number --->",odd)