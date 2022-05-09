import sys
from collections import Counter

N = int(sys.stdin.readline())
cards = sorted(Counter(map(int, sys.stdin.readline().split(" "))).items(), key= lambda x: x[0])
N = len(cards)
M = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split(" ")))

print(locals())
print(nonlocals())
print(globals())

answer = ''
for number in numbers:
    left = 0
    right = N-1
    middle = int((left+right)/2)

    # left > x: cards[x] < number
    # right < x: cards[x] > number
    while left < right:
        if number == cards[middle][0]:
            break
        elif number > cards[middle][0]:
            left = middle + 1
        else:
            right = middle - 1
        middle = int((left+right)/2)
    
    if number == cards[middle][0]:
        answer += str(cards[middle][1])+' '
    else:
        answer += '0 '
    
print(answer[:-1])