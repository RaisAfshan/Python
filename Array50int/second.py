def thirdlargest(arr):
    n=len(arr)
    arr.sort()
    return arr[n-3]
arr1=[1,2,32,44,23,54,76]
print(thirdlargest(arr1))