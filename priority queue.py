import heapq

pq = []

heapq.heappush(pq, 10)
heapq.heappush(pq, 5)
heapq.heappush(pq, 20)
heapq.heappush(pq, 1)

print("Min Priority Queue:", pq)                   #min priority queue
print("Removed Min:", heapq.heappop(pq))
print("After Deletion:", pq)







#max priority queue

import heapq

pq = []

heapq.heappush(pq, -10)
heapq.heappush(pq, -5)
heapq.heappush(pq, -20)
heapq.heappush(pq, -1)

print("Max Value:", -pq[0])

print("Removed Max:", -heapq.heappop(pq))

print("After Deletion:", [-x for x in pq])