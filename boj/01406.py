import sys


left = list(sys.stdin.readline().rstrip('\n'))
right = []
M = int(sys.stdin.readline())
commands = [line.rstrip('\n') for line in sys.stdin.readlines()]

for command in commands:
    command = command.split(" ")
    if command[0] == 'L':
        if left:
            right.append(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.pop())
    elif command[0] == 'B':
        if left:
            left.pop()
    elif command[0] == 'P':
        left.append(command[1])

print("".join(left)+"".join(right[::-1]))