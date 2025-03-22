list = ["cherry","apple","mango","banana",1,2,3,4]

list.append("blueberry")

print(list)

list1 = [5,6]

list1.extend(list)

print(list1)

list1.remove(5)
print(list1)

list1.pop(0)
print(list1)

del list[-5:]
print(list)
