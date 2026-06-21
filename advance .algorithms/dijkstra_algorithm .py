import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)
        if current_dist > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return dist

# Example
graph = {
    'A':[('B',1),('C',4)],
    'B':[('C',2),('D',5)],
    'C':[('D',1)],
    'D':[]
}
print(dijkstra(graph,'A'))  # {'A':0,'B':1,'C':3,'D':4}
