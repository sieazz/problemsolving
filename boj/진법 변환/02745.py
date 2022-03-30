import sys


N, B = sys.stdin.readline().split(" ")
N = list(N)
B = int(B)

num = 0
i = 0
while N:
    digit = N.pop()
    digit = ord(digit)-ord('A')+10 if digit.isalpha() else int(digit)
    num += digit * (B ** i)
    i += 1

print(num)
