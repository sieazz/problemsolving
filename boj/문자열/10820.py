import sys

lines = [line.rstrip('\n') for line in sys.stdin.readlines()]

for line in lines:
    alpha_low = 0
    alpha_upp = 0
    numeric = 0
    space = 0

    for ch in line:
        if ch.islower():
            alpha_low += 1
        elif ch.isupper():
            alpha_upp += 1
        elif ch.isdigit():
            numeric += 1
        else: # ch.isspace()
            space += 1
    
    print(f"{alpha_low} {alpha_upp} {numeric} {space}")
