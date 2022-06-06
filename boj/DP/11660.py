import sys


N, M = map(int, sys.stdin.readline().split())

table = [[0]*(N+1)]
for _ in range(N):
    table.append(
        [0] + list(map(int, sys.stdin.readline().split()))
    )

sums = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    row_sum = 0
    for j in range(N+1):
        row_sum += table[i][j]
        sums[i][j] = row_sum + sums[i-1][j]


def get_sum(x, y):
    return 0 if x < 0 or y < 0 else sums[x][y]
    

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(get_sum(x2, y2) - get_sum(x1-1, y2) - get_sum(x2, y1-1) + get_sum(x1-1, y1-1))
    

