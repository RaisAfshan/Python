set1 = {"apple","cherry","mango"}
set1.add('orange')
print(set1)

set2 = {1,2,3}

set1.update(set2)

print(set1)

set1.remove(1)

set1.discard(2)
set1.discard(("xyz"))
print(set1)

set1.pop()
print(set1)




