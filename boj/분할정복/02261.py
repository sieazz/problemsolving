import sys
from itertools import combinations
from typing import List


N = int(sys.stdin.readline())
points = [tuple(map(int, line.rstrip().split())) for line in sys.stdin.readlines()]
points.sort(key=lambda x: x[0])


def len_point_square(point1, point2: tuple) -> float:
    return (point2[0] - point1[0])**2 + (point2[1] - point1[1])**2


def find_nearest_pair_len(N: int, points: List) -> int:
    if len(points) < 4:
        nearest_len_square = 800000000
        for point1, point2 in combinations(points, 2):
            tmp = len_point_square(point1, point2)
            if nearest_len_square > tmp:
                nearest_len_square = tmp
        
        return nearest_len_square


    nearest_len_square = min(find_nearest_pair_len(N//2, points[:N//2]), find_nearest_pair_len(N-N//2, points[N//2:]))
    nearest_len = nearest_len_square**(1/2)
    
    x_middle = (points[N//2-1][0] + points[N//2][0])/2
    left_points, right_points = [], []
    for point in reversed(points[:N//2]):
        if x_middle - point[0] < nearest_len:
            left_points.append(point)
        else:
            break
    
    if left_points:
        left_y_min = min(left_points, key=lambda x:x[1])
        left_y_max = max(left_points, key=lambda x:x[1])
    
    for point in points[N//2:]:
        if point[0] - x_middle < nearest_len:
            if left_points and (abs(point[1] - left_y_min[1]) < nearest_len or abs(point[1] - left_y_max[1]) < nearest_len):
                right_points.append(point)
                continue
            right_points.append(point)
        else:
            break

    for lpoint in left_points:
        for rpoint in right_points:
            tmp = len_point_square(lpoint, rpoint)
            if nearest_len_square > tmp:
                nearest_len_square = tmp
    return nearest_len_square


print(find_nearest_pair_len(N, points))
            



    




