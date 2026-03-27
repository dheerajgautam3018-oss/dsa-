def example(arr):
    count = 0
    for i in range(len(arr)):        # it's time complexity=O(n)
        for j in range(len(arr)):    #it's time complexity=O(n)
            count += 1              # time complexity=O(n^2)
    return count

print(example([1,2,3]))