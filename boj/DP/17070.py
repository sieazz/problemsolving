import sys


N = int(sys.stdin.readline())
house = [list(map(int, line.split())) for line in sys.stdin.readlines()]

# pipecase[i][j] = [a,b,c]
# 파이프의 뒷끝부분이 (i, j)에 있을 때
# a = pipecase[i][j][0]: 파이프가 세로로 놓여있을 가짓수
# b = pipecase[i][j][1]: 파이프가 대각선으로 놓여있을 가짓수
# c = pipecase[i][j][2]: 파이프가 가로로 놓여있을 가짓수
pipecase = [[[0,0,0] for _ in range(N)] for _ in range(N)]
pipecase[0][1][2] = 1


def in_range(x, y):
    if x < 0 or y < 0 or x >= N or y >= N:
        return False
    return True


for i in range(N):
    for j in range(N):
        if i==0 and j==0:
            continue

        # 가로로 옮기기
        if in_range(i, j+1) and house[i][j+1] == 0:
            pipecase[i][j+1][2] = pipecase[i][j][1] + pipecase[i][j][2]

        # 세로로 옮기기
        if in_range(i+1, j) and house[i+1][j] == 0:
            pipecase[i+1][j][0] = pipecase[i][j][0] + pipecase[i][j][1]

        # 대각선으로 옮기기
        if in_range(i+1, j+1) and house[i][j+1] == 0 and house[i+1][j] == 0 and house[i+1][j+1] == 0:
            pipecase[i+1][j+1][1] = pipecase[i][j][0] + pipecase[i][j][1] + pipecase[i][j][2]


print(sum(pipecase[N-1][N-1]))
