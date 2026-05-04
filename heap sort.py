import heapq

arr = [4, 10, 3, 5, 1]
heapq.heapify(arr)

sorted_arr = []
while arr:
    sorted_arr.append(heapq.heappop(arr))

print(sorted_arr)