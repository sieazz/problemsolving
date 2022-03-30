import sys

N, K = map(int, sys.stdin.readline().split(" "))
num = list(map(int, sys.stdin.readline().split(" ")))

print(sorted(num)[K-1])
