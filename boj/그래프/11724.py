import sys
from collections import defaultdict
from typing import List


N, M = map(int, sys.stdin.readline().split(" "))
edges = [list(map(int, line.split(" "))) for line in sys.stdin.readlines()]

# # 배열 Union
# array = list(range(1,N+1)) # 1-N번째 vertex가 속해 있는 set의 번호
# array = [-1] + array

# # Union 시켜주기
# for edge in edges:
#     # edge[1]이 속하는 set을 edge[0]이 속하는 set로 편입시키기
#     array = [array[edge[0]] if array[i]==array[edge[1]] else array[i] for i in range(0, N+1)]

# print(len(set(array))-1)


def find_root(root_index: List, node: int) -> int:
    if root_index[node] == node:
        return node
    else:
        # 경로 압축 최적화(parent 노드 말고 바로 root노드로)
        # 수행시간: a(N): 에커만 함수
        root_index[node] = find_root(root_index, root_index[node])
        return root_index[node]


def union(root_index: List, a: int, b: int):
    if root_index[a] != root_index[b]:
        a_root = find_root(root_index, a)
        b_root = find_root(root_index, b)
        root_index[a_root] = b_root


root_index = list(range(N+1))
root_index[0] = -1
for edge in edges:
    union(root_index, edge[0], edge[1])

# root의 개수
cc = 0
for i in range(1, N+1):
    if i == root_index[i]:
        cc += 1
print(cc)



