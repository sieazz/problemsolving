import sys


A, B = map(int, sys.stdin.readline().split(" "))
m = int(sys.stdin.readline())
num_a = list(map(int, sys.stdin.readline().split(" ")))

num_decimal = 0
i = 0
while num_a:
    num_decimal += (A ** i) * num_a.pop()
    i += 1

num_b = []
while num_decimal:
    num_b.append(str(num_decimal % B))
    num_decimal = num_decimal // B

print(" ".join(num_b[::-1]))
