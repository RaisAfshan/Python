def secondlargest(arr):
    n = len(arr)
    arr.sort()
    for i in range(n-2,-1,-1):
        arr[i]!=arr[n-1]
        return arr[i]
    return -1

arr1 = [23,43,55,12,3,2,17]
print(secondlargest(arr1))