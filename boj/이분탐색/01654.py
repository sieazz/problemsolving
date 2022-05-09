import sys


K, N = map(int, sys.stdin.readline().split(" "))
cables = list(map(int, sys.stdin.readlines()))

low = 1
high = max(cables)+1
m = int((low+high)/2)


# 루프 불변식:
# low보다 작거나 같은 값에 대해서 sum >= N
# high보다 크거나 같은 값에 대해서 sum < N
# 종료: low+1 >= high일때... low는 sum>=N을 만족시키는 랜선길이 값 중 가장 큰 값임
while low+1 < high:
    sum = 0
    for cable in cables:
        sum += (cable // m)
    
    if sum >= N:
        low = m
    else:
        high = m
    m = int((low+high)/2)

print(low)