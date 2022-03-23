import sys


N = int(sys.stdin.readline())
paren_strings = [line.rstrip() for line in sys.stdin.readlines()]

for ps in paren_strings:
    prev_ps = ''
    while prev_ps != ps:
        prev_ps = ps
        ps = "".join(ps.split("()"))
    
    if ps:
        print("NO")
    else:
        print("YES")
