import sys
from collections import defaultdict


V = int(sys.stdin.readline())
tree = defaultdict(list)

for _ in range(V):
    line = list(map(int, sys.stdin.readline().split(" ")))
    for i in range(1, len(line)-1, 2):
        # [정점번호, 거리]
        tree[line[0]].append([line[i], line[i+1]])


# 첫 번째 DFS
# 1번 노드에서부터 가장 큰 weight를 가지는 path를 찾는다
# 발견한 path의 종점은 전체 트리에서 가장 weight가 큰 path의 끝점이다
path_len = [0 for _ in range(V+1)]
parent = [0 for _ in range(V+1)]

stack = []
stack.append(1)
while stack:
    node = stack.pop()
    for next_node, weight in tree[node]:
        if next_node != parent[node]:
            parent[next_node] = node
            path_len[next_node] = path_len[node] + weight
            stack.append(next_node)

max_node = 0
max_len = 0
for i in range(1, V+1):
    if max_len < path_len[i]:
        max_node = i
        max_len = path_len[i]


# 두 번째 DFS
# 위에서 발견한 종점을 시작으로 하는 DFS를 수행, weight가 가장 큰 path를 찾는다
path_len = [0 for _ in range(V+1)]
parent = [0 for _ in range(V+1)]

stack = []
stack.append(max_node)
while stack:
    node = stack.pop()
    for next_node, weight in tree[node]:
        if next_node != parent[node]:
            parent[next_node] = node
            path_len[next_node] = path_len[node] + weight
            stack.append(next_node)

max_node = 0
max_len = 0
for i in range(1, V+1):
    if max_len < path_len[i]:
        max_node = i
        max_len = path_len[i]

print(max_len)
