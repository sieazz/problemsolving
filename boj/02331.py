import sys


A, P = map(int, sys.stdin.readline().split(" "))
D = [A]

while True:
    new_num = 0
    for i in str(D[-1]):
        new_num += int(i)**P
    if new_num in D:
        print(D.index(new_num))
        break
    D.append(new_num)
