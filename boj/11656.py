import sys


S = sys.stdin.readline().rstrip('\n')
suffices = []

for i in range(len(S)):
    suffices.append(S[i:])

for suffix in sorted(suffices):
    print(suffix)