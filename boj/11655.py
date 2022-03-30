import sys
from itertools import cycle


string = sys.stdin.readline().rstrip('\n')
encrypted_string = ''

for ch in string:
    if ch.isalpha():
        if ch.isupper():
            cyc = cycle(range(ord('Z'), ord('A')-1, -1))
        else:
            cyc = cycle(range(ord('z'), ord('a')-1, -1))

        next_ch = chr(next(cyc))
        while next_ch != ch:
            next_ch = chr(next(cyc))
        
        for _ in range(12):
            next(cyc)
        encrypted_string += chr(next(cyc))
    else:
        encrypted_string += ch

print(encrypted_string)
