import sys
import heapq

INF = int(1e9)

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
edges = [list(map(int, line.rstrip().split())) for line in sys.stdin.readlines()]

graph = [[] for _ in range(V+1)]
for edge in edges:
    src, dest, weight = edge
    graph[src].append((dest, weight))

# table 초기화
table = [INF for _ in range(V+1)]
table[start] = 0

# heapq는 컨테이너 요소에 대해 첫 번째 요소를 기준으로 최소 힙을 구현한다
q = []
heapq.heappush(q, (0, start))

while q:
    # 조사하지 않은 노드 중 최단거리가 가장 짧은노드 선택
    cost, node = heapq.heappop(q)

    # 힙에서의 최단거리가 table의 최단거리보다 더 크다면
    # 힙에 삽입된 이후 해당 노드의 최단거리 업데이트가 이미 이루어진 경우이므로
    # 이미 조사된 노드임
    if cost > table[node]:
        continue
    
    # 현재 노드에서 갈 수 있는 다른 모든 노드에 대해 거리를 계산하고
    # 그것이 최단거리일 경우 table을 업데이트한다
    # 또한 힙에도 그 결과를 삽입한다
    for next_node, weight in graph[node]:
        if table[next_node] > cost + weight:
            table[next_node] = cost + weight
            heapq.heappush(q, (cost + weight, next_node))

for i in range(1, V+1):
    if table[i] == INF:
        print("INF")
    else:
        print(table[i])


