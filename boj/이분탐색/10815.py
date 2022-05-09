import sys

N = int(sys.stdin.readline())
my_cards = sorted(list(map(int, sys.stdin.readline().split(" "))))
M = int(sys.stdin.readline())
your_cards = list(map(int, sys.stdin.readline().split(" ")))

answer = ''
for card in your_cards:
    left = 0
    right = N-1
    middle = int((left+right)/2)

    # left > x: my_cards[x] < card
    # right < x: my_cards[x] > card
    while left < right:
        if card == my_cards[middle]:
            break
        elif card > my_cards[middle]:
            left = middle + 1
        else:
            right = middle - 1
        middle = int((left+right)/2)
    
    if card == my_cards[middle]:
        answer += '1 '
    else:
        answer += '0 '
    
print(answer[:-1])