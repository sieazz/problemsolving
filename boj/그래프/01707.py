import sys
from collections import defaultdict
from collections import deque


testcases = int(sys.stdin.readline())

for _ in range(testcases):
    V, E = map(int, sys.stdin.readline().split(" "))
    graph = defaultdict(list)
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split(" "))
        graph[u].append(v)
        graph[v].append(u)
    

    # 그룹: 음이 아닌 짝수 / 음이 아닌 홀수
    group = [-1 for _ in range(V+1)]
    result = "YES"
    while graph:
        if result == "NO":
            break

        queue = deque()
        queue.append(list(graph.keys())[0])
        group[list(graph.keys())[0]] = 0
        visited = []

        # BFS 탐색하면서 vertex의 group 지정
        while queue:
            if result == "NO":
                break

            u = queue.popleft()
            visited.append(u)
            for v in graph[u]:
                if v not in visited:
                    queue.append(v)
                if group[v] == -1:
                    group[v] = group[u]+1
                else:
                    # 연결된 vertex의 두 그룹이 동일하게 짝수거나 홀수일 시
                    # 이분그래프가 아님
                    if (group[u] + group[v]) & 1 == 0:
                        result = "NO"
                        break
            del graph[u]
    print(result)
                






    



