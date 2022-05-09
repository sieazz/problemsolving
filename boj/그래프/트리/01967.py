import sys
from collections import defaultdict


N = int(sys.stdin.readline())
tree = defaultdict(list)

edges = [list(map(int, line.split(" "))) for line in sys.stdin.readlines()]
for edge in edges:
    tree[edge[0]].append([edge[1], edge[2]])
    tree[edge[1]].append([edge[0], edge[2]])


parent = [0 for _ in range(N+1)]
path_len = [0 for _ in range(N+1)]

stack = [1]
while stack:
    node = stack.pop()
    for next_node, weight in tree[node]:
        if next_node != parent[node]:
            parent[next_node] = node
            path_len[next_node] = path_len[node] + weight
            stack.append(next_node)

max_len = 0
max_node = 0
for i in range(1, N+1):
    if max_len < path_len[i]:
        max_len = path_len[i]
        max_node = i

parent = [0 for _ in range(N+1)]
path_len = [0 for _ in range(N+1)]

stack = [max_node]
while stack:
    node = stack.pop()
    for next_node, weight in tree[node]:
        if next_node != parent[node]:
            parent[next_node] = node
            path_len[next_node] = path_len[node] + weight
            stack.append(next_node)

max_len = 0
max_node = 0
for i in range(1, N+1):
    if max_len < path_len[i]:
        max_len = path_len[i]
        max_node = i
print(max_len)