def sqr():
    list1 = []
    n = int(input("enter number of elements"))
    for i in range(n):
        element = int(input("enter the element"))
        list1.append(element)
    result =  list1[0] == list1[-1]
    print(result)
    return result
sqr()
