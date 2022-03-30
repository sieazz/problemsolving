import sys
from collections import Counter

S = sys.stdin.readline().rstrip()
c = Counter(S)

for i in range(ord('a'), ord('z')+1):
    print(c[chr(i)], end=" ")
