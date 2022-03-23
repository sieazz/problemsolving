import sys


line = sys.stdin.readline().rstrip()
line = line.replace('()', 'X') # 레이저

# 왼쪽부터 현재 놓여있는 막대기의 개수를 센다
# 레이저 기준 놓여있는 막대기의 개수가 절단 후 왼쪽에 있을 조각의 개수
# ')'는 잘려나갈 조각으로 막대기의 개수에 포함하지 않음
stick_num = 0
piece_num = 0
for c in line:
    if c == '(':
        stick_num += 1
    elif c == 'X':
        piece_num += stick_num
    else:
        piece_num += 1
        stick_num -= 1

print(piece_num)
