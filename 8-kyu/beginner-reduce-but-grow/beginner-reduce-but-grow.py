def grow(arr):
    prefix = arr[0]
    for i in range(1, len(arr)):
         
        prefix *= arr[i]
    return prefix