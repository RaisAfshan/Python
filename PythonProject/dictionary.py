mydict = {"name":"johm",
          "age": 23,
          "course":"python"}

#update
mydict["course"] = "mern"
print(mydict)

#delete
mydict.pop("age")
print(mydict)

#copy
mydict2={"age":27}
mydict2  = mydict.copy() #it overwrites
print(mydict2)

#setdefault() method
d1 = {'a': 97, 'b': 98}

print(d1.setdefault('c',9))
print(d1)

d2 ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
inventory = {"apple": 100, "orange": 80, "banana": 100}
i=inventory.popitem()
print(inventory,i)

#merge two dict also can use update() method
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merge= {**dict1,**dict2} # dict unpacking
print(merge)

merge2=dict1 | dict2
print(merge2)
