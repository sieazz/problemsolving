import sys


N, B = map(int, sys.stdin.readline().split(" "))

remainders = []
while N > 0:
    remainders.append(N % B)
    N = N // B

code = ''
while remainders:
    ch = remainders.pop()
    if ch > 9:
        code += str(chr(ord('A')+ch-10))
    else:
        code += str(ch)

print(code)
