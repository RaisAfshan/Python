friuts = ["apple","banana","cherry","grape"]

#edit:
friuts[0] = "kiwi"

print(friuts)

#no. of items from this list

print("no. of items :",len(friuts) )

#range using index
for i in range(1,4):
    print(friuts[i])

#check list is empty or not
list1 =[1]
if(list1):
    print("list is not empty")
else:
    print("list is empty")

#list of item into square
list2 = [1,2,3,4,5]
for i in list2:
    
    print("list with squareed items : ",i**2)