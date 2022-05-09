import sys
from collections import deque
from collections import defaultdict


def in_range(x, y, n):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True

n = int(sys.stdin.readline())

visited = [[False]*n for _ in range(n)]
seamap = []
for _ in range(n):
    seamap.append(list(map(int, sys.stdin.readline().split(" "))))

island_info = defaultdict(list)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

island_num = 1
for x in range(n):
    for y in range(n):
        if in_range(x, y, n) and seamap[x][y] and not visited[x][y]:
            queue = deque()
            queue.append([x, y])
            while queue:
                x_cur, y_cur = queue.popleft()
                if not visited[x_cur][y_cur]:
                    visited[x_cur][y_cur] = True
                    seamap[x_cur][y_cur] = island_num

                    # 바다에 인접한 칸만 저장해 둔다
                    near_sea = False
                    for i in range(4):
                        x_next, y_next = x_cur+dx[i], y_cur+dy[i]
                        if in_range(x_next, y_next, n):
                            if seamap[x_next][y_next] and not visited[x_next][y_next]:
                                queue.append([x_next, y_next])
                            elif seamap[x_next][y_next] == 0:
                                near_sea = True
                    
                    if near_sea:
                        island_info[island_num].append([x_cur, y_cur])

            island_num += 1


# seamap에는 지도에서 각 섬의 칸이 섬의 번호로 표시됨
# island_info에는 섬들의 칸 중 바다에 맞닿은 칸들이 각각 담김


# # 각 섬들의 바다에 인접한 칸끼리 택시거리를 구한다
# min_len = 1000
# for i in range(1, island_num-1):
#     for j in range(i+1, island_num):
#         for x1, y1 in island_info[i]:
#             for x2, y2 in island_info[j]:
#                 if min_len > abs(x2-x1) + abs(y2-y1) - 1:
#                     min_len = abs(x2-x1) + abs(y2-y1) - 1


# 각 섬들의 바다에 인접한 칸부터 시작하는 bfs 수행
min_len = 1000
for num in range(1, island_num):
    search_complete = False
    # [거리, x좌표, y좌표]
    queue = deque([0, *block] for block in island_info[num])
    while queue:
        if search_complete:
            break
        dis, x, y = queue.popleft()
        for i in range(4):
            x_next, y_next = x+dx[i], y+dy[i]
            if in_range(x_next, y_next, n):
                if abs(seamap[x_next][y_next])!=num:
                    # 다른 섬에 도착했을 경우, 그때까지의 거리가 최소인지 확인한다
                    if seamap[x_next][y_next] > 0:
                        if min_len > dis:
                            min_len = dis
                        search_complete = True
                        break
                    # 방문하지 않았던 바다의 경우, 큐에 추가해서 탐색한다
                    seamap[x_next][y_next] = - num
                    queue.append([dis+1, x_next, y_next])

print(min_len)
