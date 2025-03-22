a=[]
for i in range(4):
    element = input("enter the element of list :")
    a.append(element)

print("array = ",a)

length_element = []
for i in a:
    l=len(i)
    print(l)
    length_element.append(l)

max_length = max(length_element)
print("len of an max element",max_length)
element_max = length_element.index(max_length)
print("index of an element",element_max)

print("longest string = ",a[element_max])