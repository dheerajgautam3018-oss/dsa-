arr = [1, 2, 3, 4]

#  here we INSERT with shifting insight
index = 2
value = 99
shifts_insert = len(arr) - index   # elements  shift  in right to make space for new element

arr.insert(index, value)

print("After Insert:", arr)
print("Shifting cost (insert):", shifts_insert)


# here we DELETE with shifting insight
index = 1
shifts_delete = len(arr) - index - 1   # elements  shift left to fill the gap created by deleted element

arr.pop(index)

print("After Delete:", arr)
print("Shifting cost (delete):", shifts_delete)


# it is traverse means we are no shifting any element but we are jusst traversing the array aand printing the element one by one
print("Traversal:")
for i in arr:
    print(i)