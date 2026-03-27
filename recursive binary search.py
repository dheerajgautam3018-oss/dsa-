def binary_search(arr, low, high, x):
    
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    return -1



print(binary_search([1,2,3,4,5], 0, 4, 3))