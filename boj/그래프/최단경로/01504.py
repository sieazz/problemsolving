import sys
import heapq


INF = int(1e10)

N, E = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a].append((b, c))
    edges[b].append((a, c))
v_1, v_2 = map(int, sys.stdin.readline().split())


def dijkstra(start: int):
    table = [INF for _ in range(N+1)]
    table[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        cost, node = heapq.heappop(q)
        for next_node, weight in edges[node]:
            if cost + weight < table[next_node]:
                table[next_node] = cost + weight
                heapq.heappush(q, (cost+weight, next_node))
    
    return table


# 1에서 시작하는 다익스트라
table_1 = dijkstra(1)

# v_1에서 시작하는 다익스트라
table_v_1 = dijkstra(v_1)

# v_2에서 시작하는 다익스트라
table_v_2 = dijkstra(v_2)

answer = min(
    table_1[v_1] + table_v_1[v_2] + table_v_2[N],
    table_1[v_2] + table_v_2[v_1] + table_v_1[N]
)
if answer >= INF:
    print(-1)
else:
    print(answer)

