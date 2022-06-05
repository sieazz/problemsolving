import sys
from collections import deque

def sol():
    row, column = map(int, sys.stdin.readline().split())
    table = [list(map(int, line.rstrip())) for line in sys.stdin.readlines()]
    pathlen = [[-1]*column for _ in range(row)]
    pathlen[-1][-1] = 1

    if row==1 and column==1:
        print(1)
        return


    def in_range(x: int, y: int) -> bool:
        if x < 0 or y < 0 or x >= row or y >= column:
            return False
        return True


    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque()
    q.append((row-1,column-1))

    # 도착점을 시작으로 하는 BFS
    # 도착점으로부터의 거리 기록
    while q:
        x, y = q.popleft()
        for i in range(4):
            next_x, next_y = x+dx[i], y+dy[i]
            if in_range(next_x, next_y) and table[next_x][next_y] == 0 and pathlen[next_x][next_y] == -1:
                pathlen[next_x][next_y] = pathlen[x][y]+1
                q.append((next_x, next_y))


    # 시작점으로부터 BFS을 하면서
    # 부술 수 있는 칸을 부수고
    # 시작점~이어진 칸, 이어진 칸~도착점 까지의 거리의 합을 계산
    # 최솟값 업데이트

    if pathlen[0][0] != -1:
        minlen = pathlen[0][0]
    else: # 경로가 없었을 때
        minlen = 1000000
    
    pathlen_start = [[-1]*column for _ in range(row)]
    pathlen_start[0][0] = 1

    q = deque()
    q.append((0,0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            next_x, next_y = x+dx[i], y+dy[i]
            if in_range(next_x, next_y) and table[next_x][next_y] == 0 and pathlen_start[next_x][next_y] == -1:
                pathlen_start[next_x][next_y] = pathlen_start[x][y]+1
                q.append((next_x, next_y))
            # 벽부수기
            # 뚫리는 칸: next_x, next_y
            elif in_range(next_x, next_y) and table[next_x][next_y] == 1:
                # (next2_x, next2_y): 뚫린 칸으로부터 갈 수 있는 칸 중 도착점이란 이어진 칸
                # (0,0)~(next2_x, next2_y), (next2_x, next2_y)~도착점 까지의 거리의 합 계산
                for j in range(4):
                    next2_x, next2_y = next_x+dx[j], next_y+dy[j]
                    if in_range(next2_x, next2_y) and table[next2_x][next2_y] == 0 and pathlen_start[next2_x][next2_y] == -1 and pathlen[next2_x][next2_y] != -1:

                        if minlen > pathlen_start[x][y] + 1 + pathlen[next2_x][next2_y]:
                            minlen = pathlen_start[x][y] + 1 + pathlen[next2_x][next2_y]

    if minlen != 1000000:
        print(minlen)
    else:
        print(-1)

sol()
