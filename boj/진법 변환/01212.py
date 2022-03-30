import sys


num_bin = sys.stdin.readline().rstrip('\n')
print(bin(int(num_bin, 8))[2:])