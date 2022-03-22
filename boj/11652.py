import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
num = [int(i) for i in sys.stdin.readlines()]

# lambda x:(x[0],x[1]): x[0], x[1] 순서대로 각각 ascending하게 정렬
# lambda x:(-x[1],x[0]): x[1], x[0] 순서대로 각각 descending, ascending하게 정렬
c = sorted(Counter(num).items(), key= lambda x: (-x[1], x[0]))
print(c[0][0])

