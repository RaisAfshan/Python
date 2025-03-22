list1 = ["apple",2,"orange"]
print(list1)

a = list(("anar","cherry","watermelon"))
print(a)

a=[2,4,5,7,9]
temp = a[0]
a[0] = a[-1]
a[-1]=temp

print(a)

b=[1,2,3,4,5,6,7,8,9,10]
for i in b:
    if i % 2 ==0:
        b.pop()

print(b)

c=[1,3,5,3,4,2,2,5,6,7,7]
s=set()
dup=[]
for i in c:
    if i in s:
        dup.append(i)
    else:
        s.add(i)
print(dup)

d=[1,5,6,33,9,7,4]
maxi=max(d)
print(maxi)

# 1. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.

e=['abc', 'xyz', 'aba', '1221']
for i in e:
    if len(i)>=2:
        if i[0]==i[-1]:
            print(i)
# 2. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

f=  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list=sorted(f,key=lambda x:x[-1])
print(sorted_list)

#3 Write a Python program to check if a list is empty or not.
g=[]
# if g==[]:
#     print("empty list")
# else:
#     print('not empty')

if not g:
    print("empty")

#4 Write a Python function that takes two lists and returns True if they have at least one common member.

h1 = [3,4,3,6,8,2,6,45]
h2 = [1,3,2,4,5,6,12,13,14]
for i in h1:
    for j in h2:
        if i==j:
            result = True
            print(result)
i = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Create an empty set to store duplicate items and an empty list for unique items
dup_items = set()
uniq_items = []

# Iterate through each element 'x' in the list 'a'
for x in i:
    # Check if the current element 'x' is not already in the set 'dup_items' (it's a duplicate check)
    if x not in dup_items:
        # If 'x' is not a duplicate, add it to the 'uniq_items' list
        uniq_items.append(x)
        # Add 'x' to the 'dup_items' set to mark it as a seen item
        dup_items.add(x)

# Print the set 'dup_items' which now contains the unique elements from the original list 'a'
print(dup_items)
print(dup_items,'<== dup_items')

j=[]
if j:
    print('j is not empty')
else:
    print('j is empty')