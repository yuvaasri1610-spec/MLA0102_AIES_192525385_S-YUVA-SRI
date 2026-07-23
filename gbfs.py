import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E', 'F'],
    'D': [],
    'E': [],
    'F': []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 6,
    'E': 1,
    'F': 0
}

def greedy(start, goal):
    pq = [(heuristic[start], start)]
    visited = set()

    while pq:
        h, node = heapq.heappop(pq)

        if node in visited:
            continue

        print(node, end=" ")

        if node == goal:
            return

        visited.add(node)

        for neighbour in graph[node]:
            heapq.heappush(pq, (heuristic[neighbour], neighbour))

print("Greedy Best First Search:")
greedy('A', 'F')
