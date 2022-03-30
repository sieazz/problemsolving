import sys
import math

N = int(sys.stdin.readline())

i = 0
for digit in reversed(str(math.factorial(N))):
    if digit == '0':
        i += 1
    else:
        break

print(i)