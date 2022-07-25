import sys
from itertools import combinations


def distance(loc1, loc2):
    x1, y1 = loc1
    x2, y2 = loc2
    return abs(x2 - x1) + abs(y2 - y1)



N, M = map(int, sys.stdin.readline().split())

city = [list(map(int, line.split())) for line in sys.stdin.readlines()]

houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        if city[i][j] == 2:
            chickens.append((i, j))
            

result = int(1e9)
for chicken_case in combinations(chickens, M):
    chick_dist = 0
    for house in houses:
        chick_dist += min([distance(chicken, house) for chicken in chicken_case])
    if result > chick_dist:
        result = chick_dist

print(result)


