tuple1 = ("apple","cherry","banana")
print(tuple1)
a = tuple(("apple","mango"))
print(a)

list1  =list((tuple1))
list1.append("mango")
print(list1)

tuple1 = tuple(list1)
print(tuple1)

#1.
t1=(1,2,3,4,5,6,7,8,9)
print("t1=",t1[0])

#2.
t2=(1,3,4,)
x,y,z=t2
print("t2=",x,y,z)

#3
t3=(1,3,4,5)
li=[6,7,9]
li.extend(t3)
print("extends",li)

#convert a tuple to a string
t4=('a','b','c','d')
st=''.join(t4)
print("t4 = ",st)

#tuple to dict
t5=(('w',2),('r',5))
dict1=dict((x,y)  for x,y in t5 )
print("t5 = ",dict1)

# uzip list of tuple into individual list:
t6 = [(1,2),(4,5),(8,7)]
# li2 = list(t6)
# print(li2)
unzip = list(zip(*t6))
print(unzip)
#list of tuples to dict
li3=[("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d={}
for a,b in li3:
    d.setdefault(a,[]).append(b)#setdefault() returns the value of a key (if the key is in dictionary). Else, it inserts a key with the default value to the dictionary.
print("li3 = ",d)

# Create a list of tuples, where each tuple contains three numbers.
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# Use a list comprehension to iterate through each tuple 't' in the list 'l'.
# For each tuple, create a new tuple by removing the last element and adding the number 100.
# The result is a list of modified tuples.
print([t[:-1] + (100,) for t in l])











