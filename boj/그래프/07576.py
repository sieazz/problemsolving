import sys
from collections import deque


def in_range(x, y, row, col):
    if x<0 or y<0 or x>=row or y>=col:
        return False
    return True


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


col, row = map(int, sys.stdin.readline().split(" "))
warehouse = []
next_tomatos = []
not_rotten_num = 0
for x in range(row):
    line = list(map(int, sys.stdin.readline().split(" ")))
    warehouse.append(line)
    for y in range(col):
        if warehouse[x][y] == 1:
            next_tomatos.append([x, y])
        elif warehouse[x][y] == 0:
            not_rotten_num += 1


# 주위 토마토가 안 익었을 시 큐에 추가, 토마토를 익힘
# 주위 토마토 모두 익혔을 시 day에 1 추가
# 익힐 토마토가 없을 시 day 그대로, 루프 빠져나옴
day = 0
while next_tomatos:
    if not_rotten_num == 0:
        break
    current_tomatos = next_tomatos
    next_tomatos = []
    for tomato in current_tomatos:
        x, y = tomato[0], tomato[1]
        for i in range(4):
            x_next, y_next = x+dx[i], y+dy[i]
            if in_range(x_next, y_next, row, col) and warehouse[x_next][y_next] == 0:
                warehouse[x_next][y_next] = 1
                not_rotten_num -= 1
                next_tomatos.append([x_next, y_next])
    if next_tomatos:
        day += 1


if not_rotten_num == 0:
    print(day)
else:
    print(-1)

