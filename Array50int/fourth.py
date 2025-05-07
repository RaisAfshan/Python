#Given an array arr[] consisting of only 0’s and 1’s, the task is to find the count of a maximum number of consecutive 1’s or 0’s present in the array.

def maxConsecutiveCount(arr):
    maxCount = 0
    count = 1
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            count = count + 1
        else:
            maxCount = max(maxCount,count)
            count = 1
    return max(maxCount,count)

arr = [0,1,1,1,1,1,1,0,0,1,1,0]
print(maxConsecutiveCount(arr))
        