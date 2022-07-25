import sys
import math


data = [int(line) for line in sys.stdin.readlines()]

arr = [data[1]]
print(arr[0])
for i in range(2, data[0]+1):
    low = -1
    high = i-1
    mid = (low + high) // 2

    while low+1<high:
        if arr[mid] >= data[i]:
            high = mid
        elif arr[mid] < data[i]:
            low = mid
        mid = (low + high) // 2
    
    arr = arr[:high] + [data[i],] + arr[high:]
    print(arr[(i-1)//2])
    

