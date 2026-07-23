import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 4,
    'E': 1,
    'F': 0
}

def astar(start, goal):
    pq = [(heuristic[start], 0, start)]

    while pq:
        f, g, node = heapq.heappop(pq)

        print("Visited:", node)

        if node == goal:
            print("Goal Reached")
            print("Cost =", g)
            return

        for neighbour, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + heuristic[neighbour]
            heapq.heappush(pq, (new_f, new_g, neighbour))

print("A* Search")
astar('A', 'F')
