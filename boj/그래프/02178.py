import sys
from collections import deque


def in_range(x, y, row, col):
    if x < 0 or y < 0 or x >= row or y >= col:
        return False
    return True



row, col = map(int, sys.stdin.readline().split(" "))
maze = [list(map(int, list(line.rstrip()))) for line in sys.stdin.readlines()]
path_len = [[0]*col for _ in range(row)]


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


queue = deque()
queue.append([0, 0])
path_len[0][0] = 1

while queue:
    x, y = queue.popleft()
    if x == row-1 and y == col-1:
        print(path_len[x][y])
        break
    for i in range(4):
        x_next, y_next = x+dx[i], y+dy[i]
        if in_range(x_next, y_next, row, col) and maze[x_next][y_next] and path_len[x_next][y_next] == 0:
            path_len[x_next][y_next] = path_len[x][y]+1
            queue.append([x_next, y_next])

