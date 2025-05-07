# Given an array of integers arr[], the task is to move all the zeros to the end of the array while maintaining the relative order of all non-zero elements.

def PushZeroyoEnd(arr):
    count=0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count = count + 1

    while count < len(arr):
        arr[count] = 0
        count = count + 1

arr =  [1, 2, 0, 4, 3, 0, 5, 0]
PushZeroyoEnd(arr)
for num in arr:
    print(num,end=' ')