# heap basics
# using python's built-in min-heap implementation
 
import heapq

heap = []

heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)

print("Heap:", heap)

# get min ele without removing
print("min ele:", heap[0])

print("Heap:", heap)

# removing min ele
min_ele = heapq.heappop(heap)
print("Extracted min:", min_ele)
print("Heap after extraction:", heap)

# max-heap
mheap = []

heapq.heappush(mheap, -1)
heapq.heappush(mheap, -2)
heapq.heappush(mheap, -3)

print("mheap:", mheap)
print("max element:", -1 * heapq.heappop(mheap))
print("mheap:", mheap)