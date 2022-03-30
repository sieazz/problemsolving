import sys


N = int(sys.stdin.readline().rstrip('\n'))

remainders = []

if not N:
    remainders.append(0)

# 나머지가 무조건 음이 아니도록 나눠주어 변환을 수행
while N:
    if N & 1:
        remainders.append(1)
        N = (N-1) // (-2) 
    else:
        remainders.append(0)
        N = N // (-2)

print("".join([str(remainder) for remainder in remainders[::-1]]))

