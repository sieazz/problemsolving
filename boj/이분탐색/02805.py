import sys


N, M = map(int, sys.stdin.readline().split(" "))
# print(N, M)
trees = list(map(int, sys.stdin.readline().split(" ")))

low = 0
high = max(trees)
middle = int((low+high)/2)

while low+1 < high:
    total_len = 0
    for tree_h in trees:
        if tree_h - middle > 0:
            total_len += (tree_h - middle)
    
    # print(low, middle, high, total_len)
    if total_len == M:
        break
    elif total_len > M:
        low = middle
    else:
        high = middle
    middle = int((low+high)/2)

print(middle)
