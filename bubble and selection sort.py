# Bubble Sort
arr = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Bubble Sort:", arr)


# Selection Sort
arr2 = [64, 25, 12, 22, 11]

for i in range(len(arr2)):
    min_idx = i
    for j in range(i+1, len(arr2)):
        if arr2[j] < arr2[min_idx]:
            min_idx = j
    arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]

print("Selection Sort:", arr2)