import sys


line = sys.stdin.readline().rstrip('\n').split(" ")
print(int(line[0]+line[1]) + int(line[2]+line[3]))