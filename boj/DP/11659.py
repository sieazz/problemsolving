import sys


N, M = map(int, sys.stdin.readline().split())
table = [0] + list(map(int, sys.stdin.readline().split()))
sums = [0]
for i in range(1, N+1):
    sums.append(sums[i-1]+table[i])

for _ in range(M):
    i, j = map(int,sys.stdin.readline().split())
    print(sums[j] - sums[i-1])