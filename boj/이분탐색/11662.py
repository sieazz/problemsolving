import sys

Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, sys.stdin.readline().split())


def location_minho(t: float) -> tuple:
    return (Bx - Ax)*t + Ax, (By - Ay)*t + Ay


def location_gangho(t: float) -> tuple:
    return (Dx - Cx)*t + Cx, (Dy - Cy)*t + Cy


def difference(p1, p2: tuple) -> float:
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    return ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)


low = 0
high = 1
t1 = (low+high)/3
t2 = 2*(low+high)/3
diff1 = difference(location_minho(t1), location_gangho(t1))
diff2 = difference(location_minho(t2), location_gangho(t2))


while True:
    # 두 지점의 차가 오차범위 내
    # 두 지점의 중간값과 이차함수의 최소값의 차는 오차범위 보다 작음
    if abs(diff1 - diff2) < 10**(-6):
        diff1 =  difference(location_minho((t1+t2)/2), location_gangho((t1+t2)/2))
        break

    if diff1 >= diff2:
        low = t1
    else:
        high = t2
    t1 = low + (high-low)/3
    t2 = low + 2*(high-low)/3
    diff1 = difference(location_minho(t1), location_gangho(t1))
    diff2 = difference(location_minho(t2), location_gangho(t2))

print(f"{diff1}")

