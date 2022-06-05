import sys
import math


N = int(sys.stdin.readline())
arr = map(int, sys.stdin.readline().split(" "))

# 직접 나누기
np = 0
for i in arr:
    if i == 1:
        np += 1
        continue
    for j in range(2, (int)(math.sqrt(i))+1):
        if i % j == 0:
            print(i, j)
            np += 1
            break

# 윌슨의 정리
p = 0
for i in arr:
    if i == 1:
        continue
    if (math.factorial(i-1) + 1) % i == 0:
        p += 1

print(p)
print(N - np)