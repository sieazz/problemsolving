import sys
from collections import deque


N, K = map(int, sys.stdin.readline().rstrip('\n').split(" "))
q = deque(range(1, N+1))
josephus_seq = []
while q:
    for _ in range(K-1):
        q.append(q.popleft())
    josephus_seq.append(q.popleft())

print(f"<{str(josephus_seq)[1:-1]}>")
