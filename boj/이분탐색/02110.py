import sys
import math


# 모든 라우터 설치했을 시 True
# 설치 못한 라우터 있을 시 False
def is_installable(houses, C, distance):
    routers_left = C - 1 
    
    house1 = houses[0]
    for house2 in houses:
        if routers_left <= 0:
            break
        if house2 - house1 >= distance:
            routers_left -= 1
            house1 = house2
    
    if routers_left:
        return False
    else:
        return True


N, C = map(int, sys.stdin.readline().split(" "))
houses = sorted([int(line.rstrip()) for line in sys.stdin.readlines()])

low = 1
high = houses[-1]
middle = math.ceil((low+high)/2)

# low >= x: x보다 크거나 같은 간격으로 공유기 설치 가능
# high < x: x보다 크거나 같은 간격으로 공유기 설치 불가능
while low < high:
    if is_installable(houses, C, middle):
        low = middle
    else:
        high = middle - 1
    middle = int((low+high)/2)

print(low)
