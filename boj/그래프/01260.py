import sys
from collections import defaultdict
from collections import deque


N, M, V = map(int, sys.stdin.readline().split(" "))
edges = [list(map(int, line.split(" "))) for line in sys.stdin.readlines()]

graph = defaultdict(list)

for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

for src, dests in graph.items():
    graph[src] = sorted(dests)


# DFS(재귀)
discovered = []


def DFS(graph: dict, v: int):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            DFS(graph, w)

DFS(graph, V)
print(" ".join(map(str, discovered)))


# DFS(스택)
discovered = []
stack = []
stack.append(V)

while stack:
    v = stack.pop()
    if v not in discovered:
        discovered.append(v)
        for w in graph[v][::-1]:
            if w not in discovered[::-1]:
                stack.append(w)

print(" ".join(map(str, discovered)))


# BFS
discovered = []
queue = deque()
queue.append(V)

while queue:
    v = queue.popleft()
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered and w not in queue:
            queue.append(w)

print(" ".join(map(str, discovered)))