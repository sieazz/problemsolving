import sys

N, K = map(int, sys.stdin.readline().split())
coins = reversed([int(line) for line in sys.stdin.readlines()])

num = 0
for coin in coins:
    if K > 0:
        if K < coin:
            pass
        num += (K // coin)
        K -= coin*(K // coin)
    else: break

print(num)

