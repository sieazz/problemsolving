import sys


class Node:
    def __init__(self, num):
        self.num = num
        self.visited = False
        self.connected_with = []


N, M = map(int, sys.stdin.readline().split())

people = [Node(i) for i in range(N+1)]
num_who_know_truth = list(map(int, sys.stdin.readline().split()[1:]))

parties = []
for _ in range(M):
    tmp = list(map(int, sys.stdin.readline().split()[1:]))
    if len(tmp) > 1:
        for i in range(len(tmp)-1):
            people[tmp[i]].connected_with.append(people[tmp[i+1]])
            people[tmp[i+1]].connected_with.append(people[tmp[i]])
    
    parties.append([people[num] for num in tmp])


# 그래프 탐색
for num in num_who_know_truth:
    if people[num].visited:
        continue
    else:
        stack = []
        people[num].visited = True
        stack.append(people[num])
        while stack:
            p = stack.pop()
            for new_p in p.connected_with:
                if not new_p.visited:
                    new_p.visited = True
                    stack.append(new_p)


# 파티들을 탐색해가며 거짓말을 할 수 있는 경우인지 조사
lie_possible_case = M
for party in parties:
    for p in party:
        if p.visited:
            lie_possible_case -= 1
            break


print(lie_possible_case)

