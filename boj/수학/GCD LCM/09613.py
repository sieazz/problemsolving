import sys
from math import gcd
from itertools import combinations


N = sys.stdin.readline().rstrip()
lines = [list(map(int, line.split(" "))) for line in sys.stdin.readlines()]

for line in lines:
    gcd_sum = 0
    for combination in combinations(line[1:], 2):
        gcd_sum += gcd(combination[0], combination[1])
    print(gcd_sum)

