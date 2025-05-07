def tripletproduct(arr):
    n=len(arr)
    arr.sort()
    return max(arr[0]*arr[1]*arr[n-1],
               arr[n-1]*arr[n-2]*arr[n-3])
    # If both arr[0] and arr[1] are negative, their product is positive.
    # If multiplied by arr[n-1] (the largest number), this can be larger than the product of the top three largest numbers.

arr1=[-10, -3, 5, 6, -20]
print(tripletproduct(arr1))

