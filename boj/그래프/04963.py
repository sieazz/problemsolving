import sys
from collections import deque


def in_range(x, y, w, h):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False
    return True

while True:
    w, h = map(int, sys.stdin.readline().split(" "))
    if not w and not h:
        break
    
    visited = [[False]*w for _ in range(h)]
    seamap = []
    for _ in range(h):
        seamap.append(list(map(int, sys.stdin.readline().split(" "))))
    
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    island_num = 0
    for x in range(h):
        for y in range(w):
            if in_range(x, y, w, h) and seamap[x][y] and not visited[x][y]:
                queue = deque()
                queue.append([x, y])
                while queue:
                    x_cur, y_cur = queue.popleft()
                    if not visited[x_cur][y_cur]:
                        visited[x_cur][y_cur] = True
                        for i in range(8):
                            x_next, y_next = x_cur+dx[i], y_cur+dy[i]
                            if in_range(x_next, y_next, w, h) and seamap[x_next][y_next] and not visited[x_next][y_next]:
                                queue.append([x_next, y_next])
                island_num += 1
    print(island_num)
