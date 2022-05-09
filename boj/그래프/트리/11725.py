import sys
from collections import defaultdict


N = int(sys.stdin.readline())
edges = [list(map(int, line.split(" "))) for line in sys.stdin.readlines()]
graph = defaultdict(list)
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])


parent_node = [-1 for _ in range(N+1)]


# 루트가 1이므로 1부터 그래프 탐색을 한다
# 연결된 자식 노드들의 부모를 지정
stack = []
stack.append(1)
while stack:
    node = stack.pop()
    for next_node in graph[node]:
        if next_node != parent_node[node]:
            parent_node[next_node] = node
            stack.append(next_node)

[print(parent_node[i]) for i in range(2, N+1)]

