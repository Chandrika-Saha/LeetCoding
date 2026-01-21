from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    # directed=True -> one directional connection
    # directed=False -> two directional connection
    def add_edge(self, u, v, directed=False):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)


    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=" ")

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


g = Graph()

g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)

print("BFS:")
g.bfs(1)

print("\nDFS:")
g.dfs(1)

# BFS:
# 1 2 3 4 5
# DFS:
# 1 2 4 3 5
