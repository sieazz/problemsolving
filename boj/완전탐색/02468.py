import sys


N = int(sys.stdin.readline())

height_info = [list(map(int, line.rstrip().split())) for line in sys.stdin.readlines()]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def in_range(x, y):
    if x<0 or y<0 or x>=N or y>=N:
        return False
    return True


# 방문한 곳을 0으로 변경
def dfs(x, y, graph):
    stack = []
    stack.append((x, y))
    while stack:
        x, y = stack.pop()
        graph[x][y] = 0
        for i in range(4):
            next_x, next_y = x+dx[i], y+dy[i]
            if in_range(next_x, next_y) and graph[next_x][next_y]:
                stack.append((next_x, next_y))


area_max = 1
for water in range(1, max(max(height_info))):
    area_num = 0
    # 가라앉은 곳은 0으로 지정
    graph = [[height if height > water else 0 for height in line] for line in height_info]
    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                area_num += 1
                dfs(i, j, graph)
    area_max = area_num if area_num > area_max else area_max

print(area_max)


