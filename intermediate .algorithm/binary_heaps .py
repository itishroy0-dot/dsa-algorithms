import heapq

heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)

print(heapq.heappop(heap))  # 5
print(heapq.heappop(heap))  # 10
