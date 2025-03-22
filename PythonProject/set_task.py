

fruits ={"apple","banana","cherry"}
fruits.add("mango")
print(fruits)

#identical items into new set
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}

set3 = set1 & set2

print(set3)

#subset
setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3}
setC = {1, 2, 3, 6, 7}

print("setB is subset of setA : ", setA & setB == setB )
print("setA is subset of setB : ", setA & setB == setA )
print("setC is subset of setA : ", setA & setC == setC )

#remove duplicates
list1 = [1,2,2,3,3,4,4,4,5,6]
set1 = set(list1)
print(set1)

