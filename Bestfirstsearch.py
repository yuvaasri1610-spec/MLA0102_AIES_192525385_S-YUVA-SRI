import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 0
}

def best_first(start, goal):
    pq = [(heuristic[start], start)]
    visited = set()

    while pq:
        h, node = heapq.heappop(pq)

        print(node, end=" ")

        if node == goal:
            return

        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                heapq.heappush(pq, (heuristic[neighbour], neighbour))

print("Best First Search:")
best_first('A', 'F')
