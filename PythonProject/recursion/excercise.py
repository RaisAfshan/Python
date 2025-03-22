# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n + sum(n-1)
# print(sum(10))

#2. Write a Python program to convert an integer to a string in any base using recursion
# def string(n):
#     if n==0:
#         return 0
#     s= str(n)
#     print(type(s),s)
#     string(n-1)
#
#
# string(10)

# 3.  Write a Python program to sum recursion lists using recursion.
# Test Data: [1, 2, [3,4], [5,6]]

def sum_list(l):
    total=0
    for i in l:
        if type(i) == list:
            total=total+sum_list(i)
        else:
            total=total+i
    return total
print(sum_list([1, 2, [3,4], [5,6]]))
