import sys

N, M, K = map(int, sys.stdin.readline().split())

num = 0
while True:
    N -= 2
    M -= 1
    if N >= 0 and M >= 0 and N+M >= K:
        num += 1
    else: break

print(num)


