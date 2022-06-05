import sys


M, N = map(int, sys.stdin.readline().split(" "))


sleve = [True]*(N+1)
sleve[0], sleve[1] = False, False

for i in range(2, (int)(N**(1/2))+1):
    if sleve[i]:
        j = 2
        while i*j <= N:
            sleve[i*j] = False
            j += 1

[print(i) for i in range(M, N+1) if sleve[i]]