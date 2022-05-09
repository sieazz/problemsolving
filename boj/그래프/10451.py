import sys


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    permutation = list(map(int, sys.stdin.readline().split(" ")))
    permutation = [0] + permutation
    visited = [False] * (N+1)
    visited[0] = True
    cycle_num = 0
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            while not visited[permutation[i]]:
                i = permutation[i]
                visited[i] = True
            cycle_num += 1
    print(cycle_num)