

# n=5
# for i in range(5):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print(j+1, end=" ")
#     for j in range(i+1,n):
#         print('*',end=" ")
#     print( )

# listx = [1, 5, 7, 3, 2, 4, 6]
# sublist = listx[::2]
# print(sublist)

# sum of list:
# listx = [1, 5, 7, 3, 2, 4, 6]
# sum=1
# for i in listx:
#     sum=sum*i
#
# print(sum)

#largest nuber in list:
# listx = [1, 5, 7, 3, 2, 4, 6]
# largest = listx[0]
# print(largest)
# for i in listx:
#     if i>largest:
#         largest = i
# print(largest)

#counting start with same start and end:
# listx = ['abc', 'xyz', 'aba', '1221']
# count = 0
# for i in listx:
#     if i[0] == i[-1]:
#         count = count+1
# print(count)

#sort the tuple by last element:
# list1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# print(sorted(list1,key=lambda x:x[-1]))
#
# a = [
#     {"name": "Alice", "score": 85},
#     {"name": "Bob", "score": 91},
#     {"name": "Eve", "score": 78}
# ]
# print(sorted(a,key=lambda x:x['score']))

# Check if List is Empty
# list1=[1]
# if  list1:
#     print("list is empty")
# else:
#     print("not emplty")

#Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).
# list1 = []
# for i in range(1,31):
#     list1.append(i**2)
# print(list1[:5])
# print(list1[-5:])

for i in range(2,2):
    print(i)


