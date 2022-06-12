import sys


n = int(sys.stdin.readline())
seq = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())
num = 0


s = 0
e = n-1
while s < e:
    if seq[s] + seq[e] > x:
        e -= 1
    elif seq[s] + seq[e] < x:
        s += 1
    else:
        num += 1
        e -= 1
        s += 1

print(num)
