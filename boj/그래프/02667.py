import sys


N = int(sys.stdin.readline())
townmap = [list(map(int, list(line.rstrip()))) for line in sys.stdin.readlines()]
visited = [[False]*N for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def in_range(x: int, y: int) -> bool:
    if x < 0 or y < 0 or x >= N or y >= N:
        return False
    return True


total = 0
house_num_list = []
for x in range(N):
    for y in range(N):
        if not visited[x][y] and townmap[x][y]:
            total += 1
            house_num = 0
            stack = []
            stack.append([x, y])
            while stack:
                index = stack.pop()
                if not visited[index[0]][index[1]]:
                    house_num += 1
                    visited[index[0]][index[1]] = True
                    for i in range(4):
                        next_x, next_y = index[0]+dx[i], index[1]+dy[i]
                        if in_range(next_x, next_y) and not visited[next_x][next_y] and \
                            townmap[next_x][next_y]:
                            stack.append([next_x, next_y])
            house_num_list.append(house_num)

print(total)
[print(num) for num in sorted(house_num_list)]
                    
